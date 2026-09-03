from transmission import Transmission
from utils import load_json, closeness


class Radio:
    def __init__(self, database_path):
        data = load_json(database_path)
        self.transmissions = [
            Transmission(item)
            for item in data
        ]

        self.max_diff = 5
        self.min_signal_strength = 0.1
        self.current_freq = 0

    def tune(self, freq):
        self.current_freq = freq

    def get_signal(self):  #Returns Transmission object, float or None, None
        transmission = max(
            self.transmissions,
            key=lambda t: closeness(
                t.freq,
                self.current_freq,
                self.max_diff
            )
        )
        strength = closeness(
            transmission.freq,
            self.current_freq,
            self.max_diff
        )
        
        if strength < self.min_signal_strength:
            return None, None
        return transmission, strength
    
    def get_state(self):
        transmission, strength = self.get_signal()

        if transmission is None:
            return {
                "frequency": self.current_freq,
                "signal": None,
                "strength": 0
            }
        return {
            "frequency": self.current_freq,
            "signal": transmission.to_dict(),
            "strength": strength
        }



if __name__ == "__main__":
    radio = Radio("data/text/transmission.json")
    radio.tune(50)
    signal, strength = radio.get_signal()
    if signal:
        print(signal.content)
    else:
        print("NO SIGNAL FOUND")