from radio import Radio
from gametime import GameTime
from load_data import Transmission, Frequency
from utils import load_json
class Game:

    def __init__(self):
        data = load_json("data/text/transmission.json")
        frequencies = load_json("data/text/frequency_map_to_id.json") #static

        self.transmissions = {
            int(key): Transmission(key, value)
            for key, value in data.items()
        }
        self.frequencies = [
            Frequency(int(freq), self.transmissions[key])
            for freq, key in frequencies.items()
        ]

        self.radio = Radio(self.transmissions, self.frequencies)
        self.time = GameTime()

    def submit(self, transmission_id): #submitting transmission id deactivate it and activate the next important id
        #self.transmissions[transmission_id].deactivate()
        #I chose not to deactivate this transmission because it will be weird if the transmission suddenly disappears.

        for id, transmission in self.transmissions.items():
            if id > transmission_id and transmission.important:
                transmission.activate()
                return

        
    def update(self):
        self.time.update()

    def get_state(self):
        return {
            "time": self.time.convert_to_2359(),
            "radio": self.radio.get_state()
        }



if __name__ == "__main__":
    game = Game()
    game.radio.tune(101)
    game.transmissions[0].activate() # activating transmission 0 
    signal, strength = game.radio.get_signal()
    if signal:
        print(signal.id, signal.content, strength)
    else:
        print("NO SIGNAL FOUND")