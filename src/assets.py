import io
import json

from pygame import font, image, Surface, transform
from pygame.locals import *

from const import *


class Assets:
    def __init__(self):
        self.unextract('all')

    def extract(self, index):
        if index == 0:
            self.branding = image.load('assets/branding.png').convert_alpha()
            self.black_screen = Surface(WINDOW_SIZE)

        elif index == 1:
            with open('assets/fonts/chunk.otf', "rb") as raw: font_file = raw.read()
            self.font = font.Font(io.BytesIO(font_file), 20)

        elif index == 2:
            sheet = image.load('assets/keys_sheet.png').convert_alpha()
            with open('assets/keys_sheet.json', "rb") as raw: sheet_pos = json.loads(raw.read())

            self.sprite = {}
            default_sprite = Surface((TILE_SIZE, TILE_SIZE), SRCALPHA | RLEACCEL)
            for element, coords in sheet_pos.items():
                if len(coords) == 2:
                    x, y = coords
                    sprite = default_sprite.copy()
                    sprite.blit(sheet, (0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    self.sprite[element] = sprite

                elif len(coords) == 3:
                    x, y, w = coords
                    width_px = w * TILE_SIZE
                    sprite = Surface((width_px, TILE_SIZE), SRCALPHA | RLEACCEL)
                    sprite.blit(sheet, (0, 0), (x * TILE_SIZE, y * TILE_SIZE, width_px, TILE_SIZE))
                    self.sprite[element] = sprite

            self.title = image.load('assets/title.png').convert_alpha()
            self.title = transform.smoothscale(self.title, (self.title.get_width() / 10, self.title.get_height() / 10))

            with open('assets/fonts/chunk.otf', "rb") as raw: font_file = raw.read()
            self.font_mid = font.Font(io.BytesIO(font_file), 20)
            self.font_big = font.Font(io.BytesIO(font_file), 40)

    def unextract(self, index):
        if index in [0, 'all']:
            self.branding = None
            self.black_screen = None

        if index in [1, 'all']:
            self.font = None

        if index in [2, 'all']:
            self.sprite = dict()
            self.title = None
            self.font_mid = self.font_big = None
