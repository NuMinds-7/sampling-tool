from pygame.locals import *


class EventHandler:
    def __init__(self, app_handler):
        self.app_handler = app_handler

    def update_key(self, key):
        match self.app_handler.state:
            case 'BRANDING':
                self.app_handler.set_state('LOADING')

            case 'LOADING':
                pass

            case 'MENU':
                if key == K_UP or key == K_w:
                    self.app_handler.menu_choice -= 1
                    if self.app_handler.menu_choice < 0:
                        self.app_handler.menu_choice = 3
                elif key == K_DOWN or key == K_s:
                    self.app_handler.menu_choice += 1
                    if self.app_handler.menu_choice > 3:
                        self.app_handler.menu_choice = 0
                elif key == K_RETURN:
                    match self.app_handler.menu_choice:
                        case 0:
                            self.app_handler.set_state('MANIPULATE')
                        case 1:
                            self.app_handler.set_state('INSTRUCTIONS')
                        case 2:
                            self.app_handler.set_state('CREDITS')
                        case 3:
                            self.app_handler.set_state('QUIT')

            case 'MANIPULATE':
                if key == K_RETURN or key == K_f:
                    self.app_handler.set_state('PAUSE')
                elif key == K_UP or key == K_w:
                    pass
                elif key == K_DOWN or key == K_s:
                    pass
                elif key == K_ESCAPE:
                    self.app_handler.set_state('MENU')

            case 'INSTRUCTIONS':
                if key == K_ESCAPE:
                    self.app_handler.set_state('MENU')

            case 'CREDITS':
                if key == K_ESCAPE:
                    self.app_handler.set_state('MENU')

            case 'QUIT':
                if key == K_LEFT or key == K_a:
                    self.app_handler.quit_choice -= 1
                    if self.app_handler.menu_choice > 0:
                        self.app_handler.menu_choice = 0
                elif key == K_RIGHT or key == K_d:
                    pass
                elif key == K_RETURN:
                    pass

            case 'PAUSE':
                self.app_handler.revert_state()
