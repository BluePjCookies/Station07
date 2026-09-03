from flask import Flask, request
from radio import Radio
from gametime import Gametime

app = Flask(__name__)

# API routes here
radio = Radio("data/text/transmission.json")
gametime = Gametime()

# Get current signal
@app.route("/api/signal")
def get_signal():

    signal, strength = radio.get_signal()

    if signal:
        return {
            "signal": signal.to_dict(),
            "strength": strength
        }

    return {
        "signal": None,
        "strength": 0
    }


@app.route("/api/radio/tune", methods=["POST"])
def tune_radio():
    data = request.get_json()

    freq = data["frequency"]
    radio.tune(freq)

    return {
        "frequency": radio.current_freq
    }

@app.route("/api/game/time")
def get_game_time():
    gametime.update()

    return {
        "time": gametime.convert_to_2359()
    }

if __name__ == "__main__":
    app.run()
