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
def return_audio(filename): #return audio files within this directory. 
    return send_from_directory(os.path.join(BASE_DIR, "data/audio"), filename)

@app.route("/api/game/task/<int:task_number>")
def return_frequencies_for_task(task_number): #retrieve frequency : transmission_id key value pair
    with game_lock:
        return game.get_frequency_and_transmission_id(int(task_number))

@app.route("/api/game/transmission/<int:transmission_id>")
def return_transmission_from_id(transmission_id): #retrieve transmission detail from its id
    with game_lock:
        return game.get_transmission_from_id(int(transmission_id))

@app.route("/api/game/responses/<int:transmission_id>")
def return_transmission_responses(transmission_id): #returns the txt file for the responses.
    return send_from_directory(os.path.join(BASE_DIR, "data/text/responses"), f"{transmission_id}.txt")




if __name__ == "__main__":
    app.run()
