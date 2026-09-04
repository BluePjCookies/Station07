from flask import Flask, request
from game import Game

game = Game()

app = Flask(__name__)


@app.route("/api/radio/tune", methods=["POST"])
def tune_radio():
    data = request.get_json()

    freq = data["frequency"]
    game.radio.tune(freq)

    return {
        "frequency": game.radio.current_freq
    }

@app.route("/api/radio/submit", methods=["POST"])
def submit_transmission():
    data = request.get_json()

    transmission_id = int(data["id"])
    game.submit(transmission_id)

    return game.get_state()
    
@app.route("/api/game/state")
def get_game_state():

    game.update()
    return game.get_state()

"""
Example output
{
    "time": "22:00",
    "radio": {
        "frequency": 50,
        "signal": {
            "id": 3,
            "content": "Station 14, do you copy?",
            "freq": 50,
            "audio": "data/audio/transmission_03.mp3",
            "time" : "22:00",
            "active" : true
        },
        "strength": 1.0"
    }
}
"""

if __name__ == "__main__":
    app.run()
