from pygame.draw import rect
from pygame.transform import scale
from const import *


class DisplayHandler:
    def __init__(self, app_handler):
        self.app_handler = app_handler

    def update(self, screen):
        assets = self.app_handler.assets
        match self.app_handler.state:
            case 'BRANDING':
                screen.fill('black')
                assets.black_screen.set_alpha(255 - self.app_handler.branding_index)
                screen.blit(assets.branding, (int(WINDOW_SIZE[0] - assets.branding.get_width()) / 2, int(WINDOW_SIZE[1] - assets.branding.get_height()) / 2))
                screen.blit(assets.black_screen, (0, 0))

            case 'LOADING':
                screen.fill('black')
                bar_posx, bar_posy = int(WINDOW_SIZE[0] - LOADING_BAR_SIZE[0]) / 2, int(WINDOW_SIZE[1] - LOADING_BAR_SIZE[1]) / 2
                rect(screen, (33, 33, 255), (bar_posx - 4, bar_posy - 4) + (LOADING_BAR_SIZE[0] + 8, LOADING_BAR_SIZE[1] + 8), width = 2)
                rect(screen, (33, 33, 255), (bar_posx, bar_posy) + (LOADING_BAR_SIZE[0] * (self.app_handler.loading_index / 100), LOADING_BAR_SIZE[1]))

                txt = assets.font.render('LOADING...', True, (33, 33, 255))
                screen.blit(txt, (bar_posx + int(LOADING_BAR_SIZE[0] - txt.get_width()) / 2, bar_posy - LOADING_BAR_SIZE[1] - 4))
                txt = assets.font.render(str(self.app_handler.loading_index) + '%', True, 'white')
                screen.blit(txt, (bar_posx + int(LOADING_BAR_SIZE[0] - txt.get_width()) / 2, bar_posy))

            case 'MENU':
                screen.fill('black')
                screen.blit(assets.title, (int(WINDOW_SIZE[0] - assets.title.get_width()) / 2, 60))
                screen.blit(assets.font.render('MANIPULATE', True, 'white' if self.app_handler.menu_choice == 0 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (265, 260))
                screen.blit(assets.font.render('INSTRUCTIONS', True, 'white' if self.app_handler.menu_choice == 1 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (265, 290))
                screen.blit(assets.font.render('CREDITS', True, 'white' if self.app_handler.menu_choice == 2 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (265, 320))
                screen.blit(assets.font.render('EXIT', True, 'white' if self.app_handler.menu_choice == 3 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (265, 350))

            case 'MANIPULATE':
                screen.fill('black')
                screen.blit(assets.font_big.render('MANIPULATE', True, (192, 192, 0)), (20, 20))
                screen.blit(assets.font_mid.render('CURRENT DIRECTION: N/A', True, (192, 192, 0)), (20, 416))
                screen.blit(assets.font_mid.render('SCRAPING: NO', True, (192, 192, 0)), (20, 446))

            case 'INSTRUCTIONS':
                screen.fill('black')
                screen.blit(assets.font_big.render('USER MANUAL', True, (192, 192, 0)), (20, 20))
                screen.blit(assets.font_mid.render('MOVEMENT KEYS', True, (192, 192, 0)), (20, 70))
                screen.blit(scale(assets.sprite['k_W'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_W_p'], (32, 32)), (20, 100))
                screen.blit(scale(assets.sprite['k_UP'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_UP_p'], (32, 32)), (55, 100))
                screen.blit(assets.font.render('WHEELS FORWARD', True, 'white'), (95, 104))
                screen.blit(scale(assets.sprite['k_S'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_S_p'], (32, 32)), (20, 140))
                screen.blit(scale(assets.sprite['k_DOWN'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_DOWN_p'], (32, 32)), (55, 140))
                screen.blit(assets.font.render('WHEELS BACKWARD', True, 'white'), (95, 144))

                screen.blit(assets.font_mid.render('LATHE MANIPULATION', True, (192, 192, 0)), (20, 194))
                screen.blit(scale(assets.sprite['k_SPACE'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_SPACE_p'], (208, 32)), (20, 224))
                screen.blit(assets.font.render('SPIN ON/OFF', True, 'white'), (236, 228))

                screen.blit(assets.font_mid.render('EMERGENCY STOP', True, (192, 192, 0)), (20, 278))
                screen.blit(scale(assets.sprite['k_F'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_F_p'], (32, 32)), (20, 308))
                screen.blit(scale(assets.sprite['k_RETURN'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_RETURN_p'], (68, 32)), (55, 308))
                screen.blit(assets.font.render('TERMINATE ALL', True, 'white'), (131, 312))
                screen.blit(scale(assets.sprite['k_Q'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_Q_p'], (32, 32)), (20, 348))
                screen.blit(assets.font.render('FORCE QUIT', True, 'white'), (60, 352))

                screen.blit(assets.font_mid.render('MISC KEYS', True, (192, 192, 0)), (360, 70))
                screen.blit(scale(assets.sprite['k_ESCAPE'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_ESCAPE_p'], (32, 32)), (360, 100))
                screen.blit(assets.font.render('RETURN TO MENU', True, 'white'), (400, 104))
                screen.blit(scale(assets.sprite['k_M'] if int(self.app_handler.animation_index) % 48 < 24 else assets.sprite['k_M_p'], (32, 32)), (360, 140))
                screen.blit(assets.font.render('PLAY MUSIC', True, 'white'), (400, 144))

            case 'CREDITS':
                screen.fill('black')
                screen.blit(assets.font_big.render('CREDITS', True, (192, 192, 0)), (20, 20))
                screen.blit(assets.font_mid.render('PREPARED FOR CLIENT', True, (192, 192, 0)), (20, 70))
                screen.blit(assets.font.render('SCOTT READ', True, 'white'), (20, 95))

                screen.blit(assets.font_mid.render('TEAM MEMBERS', True, (192, 192, 0)), (20, 145))
                screen.blit(assets.font.render('PUI WING CHUNG', True, 'white'), (20, 170))
                screen.blit(assets.font.render('NATHAN FORAN', True, 'white'), (20, 195))
                screen.blit(assets.font.render('EMILY LIN', True, 'white'), (20, 220))
                screen.blit(assets.font.render('TALEN TSIGARIS', True, 'white'), (20, 245))

                screen.blit(assets.font.render('HOUSING SYSTEM', True, 'white'), (220, 170))
                screen.blit(assets.font.render('POWER SUPPLY', True, 'white'), (220, 195))
                screen.blit(assets.font.render('QUALITY CONTROL', True, 'white'), (220, 220))
                screen.blit(assets.font.render('ARDUINO & SOFTWARE', True, 'white'), (220, 245))

                screen.blit(assets.font_mid.render('SPECIAL THANKS TO', True, (192, 192, 0)), (20, 295))
                screen.blit(assets.font.render('DAVID KNOX', True, 'white'), (20, 320))
                screen.blit(assets.font.render('AARANI GOWRYSHANKAR', True, 'white'), (20, 345))
                screen.blit(assets.font.render('FARNAZ JAZAERI', True, 'white'), (20, 370))
                screen.blit(assets.font.render('OLIVIA POOLER', True, 'white'), (20, 395))

            # case 'QUIT':
            #     screen.blit(rect(screen, ))

            case 'PAUSE':
                text_pause_shadow = assets.font_big.render('PAUSED', True, (0, 0, 64))
                text_pause = assets.font_big.render('PAUSED', True, 'white' if int(self.app_handler.animation_index) % 3 else (33, 33, 255))
                screen.blit(text_pause_shadow, (int(WINDOW_SIZE[0] - text_pause.get_width()) / 2 - 8, int(WINDOW_SIZE[1] - text_pause.get_height()) / 2 - 8))
                screen.blit(text_pause, (int(WINDOW_SIZE[0] - text_pause.get_width()) / 2, int(WINDOW_SIZE[1] - text_pause.get_height()) / 2))
