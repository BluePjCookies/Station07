import os
import threading

from flask import Flask, request, send_from_directory
from game import Game

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

game = Game()
# One shared Game means one shared radio dial and clock, so every request that
# touches it has to take this lock. Run the server single-worker (each worker
# process would otherwise get its own Game and players would flip between them).
game_lock = threading.Lock()

app = Flask(__name__, static_folder="frontend", static_url_path="")


@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/data/audio/<path:filename>")
def audio(filename):
    return send_from_directory(os.path.join(BASE_DIR, "data/audio"), filename)

@app.route("/api/radio/tune", methods=["POST"])
def tune_radio():
    data = request.get_json()

    freq = data["frequency"]

    with game_lock:
        game.radio.tune(freq)

        return {
            "frequency": game.radio.current_freq
        }

@app.route("/api/radio/submit", methods=["POST"])
def submit_transmission():
    data = request.get_json()

    transmission_id = int(data["id"])

    with game_lock:
        game.submit(transmission_id)
        return game.get_state()

@app.route("/api/game/state")
def get_game_state():

    with game_lock:
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
            "audio": "data/audio/transmission_03.mp3",
            "active" : true
        },
        "strength": 1.0"
    }
}
"""

if __name__ == "__main__":
    app.run()
