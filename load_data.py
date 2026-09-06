class Transmission:
    def __init__(self, key, data):
        self.id = int(key)
        self.content = data["content"]
        self.task = int(data["task"])
        self.important = data["important"]

    def __str__(self):
        return f"Transmission {self.id}: {self.content}"
    
    def to_dict(self): #Return dictionary to FLASK API
        return {
            "id": self.id,
            "content": self.content,
            "audio": f"data/audio/transmissions/{self.id}.mp3",
            "task" : self.task,
            "important" : self.important,
            "response" : f"data/text/responses/{self.id}.txt"
        }

class Frequency:

    def __init__(self, freq, transmission):
        self.freq = float(freq)
        self.transmission = transmission

    def get_active_transmission(self, task:int): # return transmissions of specific task int
        if self.transmission and self.transmission.task == task:
            return self.transmission

        return None
    