import os
from load_data import Transmission, Frequency
from utils import load_json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Game:

    def __init__(self):
        transmissions = load_json(os.path.join(BASE_DIR, "data/text/transmission.json"))
        frequencies = load_json(os.path.join(BASE_DIR, "data/text/frequency_map_to_id.json")) #static

        self.transmissions = {
            int(id): Transmission(id, transmission)
            for id, transmission in transmissions.items()
        } #dictionary of transmission_id and transmission object
        self.frequencies = [
            Frequency(float(freq), self.transmissions[int(transmission_id)])
            for freq, transmission_id in frequencies.items()
        ] #list of frequency objects

    def get_transmission_from_id(self, id): #retrieve transmission details from transmission id
        return self.transmissions[int(id)].to_dict()
    
    def get_frequency_and_transmission_id(self, task_number:int): # get array of freq:id corresponding to task_number n -> List(Dict)
            frequency_and_transmission = []
            for frequency in self.frequencies:
                transmission = frequency.get_active_transmission(task_number)
                if transmission:
                    new_data = {"frequency": frequency.freq, "transmission id": transmission.id}
                    frequency_and_transmission.append(new_data)
    
            return frequency_and_transmission

if __name__ == "__main__":
    game = Game()
    print(game.get_transmission_from_id(4))
    print(game.get_frequency_and_transmission_id(2))