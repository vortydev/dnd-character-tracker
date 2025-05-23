# D&D Character Tracker
I've started the very laborious task to make my own character tracker for Dungeons & Dragons 5e.

The system is fully modular with a OOP approach.

*I work on this project on my spare time!*

## Setup
### Requirements
- Python installed on your system (minimum v3.10)
- Bash

### Building necessary files
The first step is to build the JSON files containing the data needed by the various Registry objects.

Simply execute the following script :
```bash
bash tools/build_all.sh
```

Once that's done, enter the `./bin` folder, and you can run the Tracker program :
```python
python tracker.py
```

## Feature List
