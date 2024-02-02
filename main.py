import pygame
import configs
import assets

from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird

pygame.init()

screen_size = (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)

Clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
pygame.time.set_timer(column_create_event, 1500)

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()

Background(0, sprites)
Background(1, sprites)

Floor(0, sprites)
Floor(1, sprites)

bird = Bird(sprites)

score = 0
running = True
game_over = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == column_create_event:
      Column(sprites)
      
    bird.handle_flap_event(event)
 
  screen.fill('pink')
  sprites.draw(screen)

  if not game_over:
    sprites.update()
  
  if bird.check_collision(sprites):
    game_over = True
    
  for sprite in sprites:
    if type(sprite) is Column and sprite.is_passed():
      score += 1
      print(score)
  
  pygame.display.flip()
  Clock.tick(configs.FPS)

pygame.quit()