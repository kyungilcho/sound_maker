from constants import NOTE_DURATION

class Note:
    def __init__(self, name: str, duration: float = 1):
        self.name = name
        self.duration = duration * NOTE_DURATION

    def get_frequency(self):
        note = self.name.strip().upper()

        # Handle REST (no frequency)
        if note == "REST":
            return 0  # Or you can return 0 or another sentinel value
        
        # Extract the parts of the note
        if len(note) == 2:
            pitch = note[0]
            octave = int(note[1])
        elif len(note) == 3:
            pitch = note[0:2]
            octave = int(note[2])
        else:
            raise ValueError("Invalid note format. Examples of valid notes: C4, A#3, Db5")
        
        # Get the semitone offset from A4
        if pitch not in NOTE_SEMITONE_MAP:
            raise ValueError(f"Invalid pitch: {pitch}")
        
        semitone_offset = NOTE_SEMITONE_MAP[pitch]
        
        # Calculate the total number of semitones from A4
        n = semitone_offset + (octave - 4) * 12
        
        # Calculate the frequency
        frequency = 440 * (2 ** (n / 12))
        
        return frequency
    

NOTE_SEMITONE_MAP = {
    'C': -9,
    'C#': -8,
    'Db': -8,
    'D': -7,
    'D#': -6,
    'Eb': -6,
    'E': -5,
    'F': -4,
    'F#': -3,
    'Gb': -3,
    'G': -2,
    'G#': -1,
    'Ab': -1,
    'A': 0,
    'A#': 1,
    'Bb': 1,
    'B': 2
}