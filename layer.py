from enum import IntEnum, auto

class Layer(IntEnum):
  BACKGROUND = auto()
  OBSTACLE = auto()
  FLOOR = auto()
  BIRD = auto()
  UI = auto()
