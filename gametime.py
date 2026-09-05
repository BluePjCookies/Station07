# Deals with game time
import time


class GameTime:

    def __init__(self):
        self.start_game_time = 22*60*60 # Starts at 10pm
        self.time_scale = 120 #Every 1 seconds is 2 min game time
        # monotonic() instead of time(), so an NTP correction or a machine
        # waking from sleep can't make the clock jump or run backwards.
        self.start_real_time = time.monotonic()

    def get_time(self):
        # Derived from the start point rather than accumulated, so the answer
        # doesn't depend on how often (or whether) anything asks for it.
        elapsed = time.monotonic() - self.start_real_time

        return self.start_game_time + elapsed * self.time_scale

    def convert_to_2359(self) -> str:
        game_time = self.get_time()

        hours = int(game_time // 3600) % 24 # wrap past midnight instead of 24:00, 25:00...
        minutes = int((game_time % 3600) // 60)

        return f"{hours:02d}:{minutes:02d}"

if __name__ == "__main__":
    game = GameTime()
    time.sleep(7)
    print(game.convert_to_2359())
