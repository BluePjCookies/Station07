# Deals with game time
import time


class GameTime:

    def __init__(self):
        self.game_time = 22*60*60 # Starts at 10pm
        self.time_scale = 120 #Every 1 seconds is 2 min game time
        self.last_time = time.time()

    def update(self):
        current_time = time.time()
        dt = current_time - self.last_time
        self.last_time = current_time

        self.game_time += dt * self.time_scale

    def get_time(self):
        return self.game_time

    def convert_to_2359(self) -> str:
        hours = int(self.game_time // 3600) % 24 # wrap past midnight instead of 24:00, 25:00...
        minutes = int((self.game_time % 3600) // 60)

        return f"{hours:02d}:{minutes:02d}"

if __name__ == "__main__":
    game = GameTime()
    time.sleep(7)
    game.update()
    print(game.convert_to_2359())