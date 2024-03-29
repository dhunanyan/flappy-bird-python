import pygame
import assets
import config

from layer import Layer
from objects.floor import Floor
from objects.column import Column

class Bird(pygame.sprite.Sprite):
  def __init__(self, *groups):
    self._layer = Layer.BIRD
    
    self.images = [
      assets.get_sprite("redbird-upflap"),
      assets.get_sprite("redbird-midflap"),
      assets.get_sprite("redbird-downflap")
    ]
    
    self.flap = 0
    self.image_index = 0
    self.image = self.images[self.image_index]
    self.rect = self.image.get_rect(topleft=(-50, 50))
    
    self.mask = pygame.mask.from_surface(self.image)
    
    super().__init__(*groups)
    
  def update(self):
    self.image_index += 1
    self.image_index = self.image_index
    if self.image_index // config.BIRD_ANIMATION_SPEED > len(self.images) - 1:
      self.image_index = 0
    self.image = self.images[self.image_index // config.BIRD_ANIMATION_SPEED]
    
    self.flap += config.GRAVITY
    self.rect.y += self.flap
    
    if self.rect.x < config.BIRD_Y_POSITION:
      self.rect.x += config.BIRD_APPEARING_SPEED
    
  def handle_flap_event(self, event, game_over):
    if event.type == pygame.KEYDOWN and event.key == getattr(pygame, config.FLAP_KEY):
      self.flap = 0
      self.flap -= config.BIRD_FLAP_RADIUS
      if not game_over:
        assets.play_audio('wing')
      
  def check_collision(self, sprites):
    for sprite in sprites:
      is_column = type(sprite) is Column
      is_floor = type(sprite) is Floor
      x_y_diff = (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y)
      
      if ((is_column or is_floor) and 
        sprite.mask.overlap(self.mask, x_y_diff) or 
        self.rect.bottom < 0):
        return True
    return False