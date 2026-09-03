from radio import Radio
from gametime import GameTime

class Game:

    def __init__(self):
        self.time = GameTime()
        self.radio = Radio("data/text/transmission.json")
        
    def update(self):
        self.time.update()

    def get_state(self):
        return {
            "time": self.time.convert_to_2359(),
            "radio": self.radio.get_state()
        }