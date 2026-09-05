class Transmission:
    def __init__(self, key, data):
        self.id = int(key)
        self.audio = data["audio"]
        self.content = data["content"]
        self.active = data["active"]
        self.important = data["important"]

    def __str__(self):
        return f"Transmission {self.id}: {self.content}"

    def activate(self):
        self.active = True

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "audio": self.audio,
            "active" : self.active,
            "important" : self.important
        }

class Frequency:

    def __init__(self, freq, transmission):
        self.freq = int(freq)
        self.transmission = transmission

    def get_active_transmission(self):
        if self.transmission and self.transmission.active:
            return self.transmission

        return None
    