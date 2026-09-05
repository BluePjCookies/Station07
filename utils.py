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
