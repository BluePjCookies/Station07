# Template for Transmission

class Transmission:
    def __init__(self, data):
        self.id = data["id"]
        self.freq = data["freq"]
        self.time = data["time"]
        self.audio = data["audio"]
        self.content = data["content"]
        return
    
    def __str__(self):
        return f"Transmission {self.id}: {self.content}"

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "freq": self.freq,
            "audio": self.audio,
            "time": self.time
        }
    

    