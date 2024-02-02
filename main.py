import pygame
import config
import assets

from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.game_over_message import GameOverMessage
from objects.game_start_message import GameStartMessage
from objects.score import Score

pygame.init()

screen_size = (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)

Clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT

assets.load_sprites()
assets.load_audios()

sprites = pygame.sprite.LayeredUpdates()

def create_sprites():
  Background(0, sprites)
  Background(1, sprites)

  Floor(0, sprites)
  Floor(1, sprites)

  return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_started_message, score = create_sprites()

running = True
game_over = False
game_started = False
FPS = config.FPS
high_score = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == column_create_event:
      Column(sprites)
    if event.type == pygame.KEYDOWN:
      if event.key == getattr(pygame, config.FLAP_KEY) and not game_started and not game_over:
        game_started = True
        game_started_message.kill()
        pygame.time.set_timer(column_create_event, 1500)
      if event.key == getattr(pygame, config.CLOSE_KEY) and game_over:
        if score.value > high_score:
          high_score = score.value
        config 
        FPS = config.FPS
        game_over = False
        game_started = False
        sprites.empty()
        bird, game_started_message, score = create_sprites()
      
    bird.handle_flap_event(event, game_over)
 
  screen.fill('pink')
  sprites.draw(screen)

  if game_started and not game_over:
    sprites.update()
  
  if bird.check_collision(sprites) and not game_over:
    game_over = True
    game_started = False
    GameOverMessage(sprites)
    pygame.time.set_timer(column_create_event, 0)
    assets.play_audio('hit')
    
  for sprite in sprites:
    if type(sprite) is Column and sprite.is_passed():
      if config.FPS < 100:
        FPS += 0.1
      score.value += 1
      assets.play_audio('point')
  
  pygame.display.flip()
  Clock.tick(FPS)

pygame.quit()