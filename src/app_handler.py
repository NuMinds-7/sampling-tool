from pygame import quit as pyquit
import sys
import threading

from assets import *
from schedule import *


class AppHandler:
    def __init__(self):
        self.assets = Assets()
        self.assets.extract(0)
        self.assets.extract(1)
        self.state = 'BRANDING'
        self.old_state = ''
        self.animation_index = 0
        self.branding_index = 0
        self.loading_index = 0
        self.menu_choice = 0
        self.credit_offset = 0

    def loading(self):
        self.assets.unextract(0)
        self.assets.extract(2)
        Schedule.load_finished = True

    def set_state(self, state):
        self.old_state, self.state = self.state, state

    def revert_state(self):
        self.old_state, self.state = self.state, self.old_state

    def update(self):
        self.animation_index += .2
        match self.state:
            case 'BRANDING':
                self.branding_index += 1
                if self.branding_index > 255:
                    self.set_state('LOADING')

            case 'LOADING':
                if not Schedule.load_started:
                    Schedule.load_started = True
                    threading.Thread(target=AppHandler.loading, args=(self,)).start()

                self.loading_index += 1
                if self.loading_index > 100:
                    self.loading_index = 100
                    if Schedule.load_finished:
                        self.set_state('MENU')

            case 'MANIPULATE':
                pass  # TODO

            case 'QUIT':
                # TODO: Send popup
                pyquit()
                sys.exit()
