import numpy as np
from constants import AMPLITUDE, SAMPLE_RATE
import sounddevice as sd
from notes_refactored import Note
from notes import NOTES

def generate_pulse_wave(frequency, duration, sample_rate=44100, duty_cycle=0.5):
    """Generate a pulse wave with a given frequency and duration."""
    if frequency == 0:  # Rest note
        return np.zeros(int(duration * sample_rate))
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.where(np.sin(2 * np.pi * frequency * t) > 2 * duty_cycle - 1, 1, -1)
    return AMPLITUDE * wave

def combine_notes(sequence, sample_rate=44100):
    """Combine multiple notes into a single waveform."""
    combined_wave = np.array([])
    for note, duration in sequence:
        wave = generate_pulse_wave(NOTES[note], duration, sample_rate)
        combined_wave = np.concatenate((combined_wave, wave))
    return combined_wave

## create a sequence from a list of measures
def create_sequence(measures: list[list[tuple[str, float]]]):
    sequence: list[tuple[str, float]] = []
    for measure in measures:
        sequence.extend(measure)
    return sequence

def play_sequence(sequence: list[tuple[str, float]], sample_rate: int = SAMPLE_RATE):
    sd.play(combine_notes(sequence, sample_rate), sample_rate)
    sd.wait()
    
    
    
#########################################    
    
    
    
def combine_notes_refactored(sequence: list[Note], sample_rate: int = SAMPLE_RATE):
    combined_wave = np.array([])
    for note in sequence:
        wave = generate_pulse_wave(note.get_frequency(), note.duration, sample_rate)
        combined_wave = np.concatenate((combined_wave, wave))
    return combined_wave

def play_sequence_refactored(sequence: list[Note], sample_rate: int = SAMPLE_RATE):
    sd.play(combine_notes_refactored(sequence, sample_rate), sample_rate)
    sd.wait()
    
def create_sequence_refactored(measures: list[list[Note]]):
    sequence: list[Note] = []
    for measure in measures:
        sequence.extend(measure)
    return sequence