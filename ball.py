from pico2d import *
from background import FixedBackground as back
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.sx = 0
        self.sy = 0




    def draw(self):
        bg_window_l = server.boy.bg.window_left
        bg_window_b = server.boy.bg.window_bottom
        self.sx = self.x - bg_window_l
        self.sy = self.y - bg_window_b
        self.image.draw(self.sx, self.sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)