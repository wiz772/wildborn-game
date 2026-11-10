import pygame

FPS = 60
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_NAME = "WildBorn"

WORLD_SIZE = (100,100)

CHOICE_KEYS = {
    pygame.KSCAN_1: 0,
    pygame.KSCAN_2: 1,
    pygame.KSCAN_3: 2
}

HUD_TEXT_COLOR = ((0,30,0))

DATA_FILE_PATH  = "data/scores.json"