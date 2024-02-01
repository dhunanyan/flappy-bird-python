import pygame
import configs
import assets

from objects.background import Background

pygame.init()

screen_size = (configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT)
screen = pygame.display.set_mode(screen_size)
Clock = pygame.time.Clock()
running = True

assets.load_sprites()
sprites = pygame.sprite.LayeredUpdates()

Background(sprites)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill('pink')
  
  sprites.draw(screen)
  
  pygame.display.flip()
  Clock.tick(configs.FPS)

pygame.quit()