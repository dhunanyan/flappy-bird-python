import pygame
import config
import assets
from layer import Layer

class GameOverMessage(pygame.sprite.Sprite):
  def __init__(self, *groups):
    self._layer = Layer.UI
    self.image = assets.get_sprite('game_over')
    self.rect = self.image.get_rect(center=(config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2))
    self.mask = pygame.mask.from_surface(self.image)
    
    super().__init__(*groups)
    
  