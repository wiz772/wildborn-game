from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    PAUSED = auto()
    LEVEL_UP = auto()
    GAME_OVER = auto() 