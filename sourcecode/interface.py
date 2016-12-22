from pico2d import*
import init

import start_state


class Volume:
    def __init__(self):
        self.volume_frame = 0
        self.image = load_image("vol.png")

    def update(self, frame_time):
        pass

    def draw(self):
        self.image.clip_draw(self.volume_frame * 100, 0, 100, 100, 70, 530)

        if start_state.volume < 20:
            self.volume_frame = 0
        if start_state.volume < 15:
            self.volume_frame = 1
        if start_state.volume < 10:
            self.volume_frame = 2
        if start_state.volume < 1:
            self.volume_frame = 3


class Wasted:
    def __init__(self):
        self.x, self.y = 400, 400
        self.image = load_image("wasted.png")

    def update(self, frame_time):
        pass

    def draw(self):
        if init.life == 0:
            self.image.draw(self.x, self.y)
            init.wasted_state = 1
