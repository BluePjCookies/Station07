
from utils import get_strength
import random

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
        # Only frequencies that are actually broadcasting can be picked up, so a
        # silent station never masks a live one that is also within range.
        best = None
        best_strength = 0

        for frequency in self.frequencies:
            transmission = frequency.get_active_transmission()

            if transmission is None:
                continue

            strength = get_strength(
                frequency.freq,
                self.current_freq,
                self.max_diff
            )

            if strength > best_strength:
                best = transmission
                best_strength = strength

        if best_strength < self.min_signal_strength:
            return None, random.random()/10

        return best, best_strength
    
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

