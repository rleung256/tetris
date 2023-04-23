from settings import *
import random


class Block(pg.sprite.Sprite):  # inheriting from spite class from pygame
    def __init__(self, tetrimino, pos):
        self.tetromino = tetrimino
        self.pos = vec(pos) + INIT_POS_OFFSET

        super().__init__(tetrimino.tetris.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('orange')

        self.rect = self.image.get_rect()
        # the line below is made possible by vector look into that if we care in the future
        self.rect.topleft = self.pos * TILE_SIZE


class Tetrimino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(TETROMINOES.keys()))
        self.blocks = [Block(self, pos) for pos in TETROMINOES[self.shape]]

    def update(self):
        pass
