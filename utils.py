import json
import os

def load_json(path): # easy way to load json scripts (Satisfy file imports requirements)
    
    if not os.path.isfile(path):
        raise Exception(f"No file at {path}")
        
    
    with open(path, "r") as f:
        return json.load(f)

# define how close two values are. Scales from 0 to 1. 0 when the difference = Max distance and 1 when value -target = 0
def get_strength(value, target, max_diff):
    return max(0, 1 - abs(value - target) / max_diff)

from pydub import AudioSegment

input_file = "data/audio/static.mp3"
output_file = "data/audio/static_update.mp3"
increase_db = 10  # Increase volume by 10 dB

audio = AudioSegment.from_mp3(input_file)
louder_audio = audio + increase_db
louder_audio.export(output_file, format="mp3")

print(f"Done! Saved as {output_file}")