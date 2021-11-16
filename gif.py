import bird_familiar as bird

class Gif:
    def __init__(self, type):
        self.type = type

        if self.type == "bird_familiar":
            self.idle_frames = bird.idle_frames
            self.idle_to_sleep_frames = bird.idle_to_sleep_frames
            self.sleep_frames = bird.sleep_frames
            self.sleep_to_idle_frames = bird.sleep_to_idle_frames
            self.left_frames = bird.left_frames
            self.right_frames = bird.right_frames