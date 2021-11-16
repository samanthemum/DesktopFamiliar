import bird_familiar as bird
import random

class Gif:

    # CONSTANTS: should be same likelihood regardless of gif
    idle_num = [1,2,3,4]
    sleep_num = [10,11,12,13,15]
    sleep_to_idle_num = 14
    idle_to_sleep_num = 5
    walk_left = [6,7]
    walk_right = [8,9]

    def __init__(self, type):
        self.type = type

        if self.type == "bird_familiar":
            self.idle_frames = bird.idle_frames
            self.idle_to_sleep_frames = bird.idle_to_sleep_frames
            self.sleep_frames = bird.sleep_frames
            self.sleep_to_idle_frames = bird.sleep_to_idle_frames
            self.left_frames = bird.left_frames
            self.right_frames = bird.right_frames

            self.x = 1400
            self.event_number = random.randrange(1, 3, 1)
            self.cycle = 0
            self.check = 1