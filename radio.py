
from utils import get_strength


class Radio:

    def __init__(self, transmissions, frequencies):
        self.current_freq = 0
        self.max_diff = 5
        self.min_signal_strength = 0.1
        self.frequencies = frequencies
        self.transmissions = transmissions

    def tune(self, freq):
        self.current_freq = freq

    def get_signal(self):

        frequency = min(
            self.frequencies,
            key=lambda f: abs(f.freq - self.current_freq)
        )

        strength = get_strength(
            frequency.freq,
            self.current_freq,
            self.max_diff
        )

        if strength < self.min_signal_strength:
            return None, 0

        transmission = frequency.get_active_transmission()

        if transmission is None:
            return None, 0

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

