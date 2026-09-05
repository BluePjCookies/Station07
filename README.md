```text
Station07/
│
├── main.py                  # Flask API / application entry point
├── game.py                  # Main game controller
│
├── gametime.py              # Manages game time
├── radio.py                 # Radio system
├── load_data.py             # Transmission and Frequency objects
│
├── utils.py                 # Helper functions
│
└── data/
    ├── audio/               # Transmission audio files
    └── text/
        ├── transmission.json           # Transmission content, keyed by id
        └── frequency_map_to_id.json    # Maps a radio frequency to a transmission id
```
