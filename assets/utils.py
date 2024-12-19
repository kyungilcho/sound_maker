import numpy as np
from constants import AMPLITUDE, SAMPLE_RATE, NOTE_DURATION
import sounddevice as sd
from notes_refactored import Note
from notes import NOTES
from enum import Enum
from piano_sound import generate_piano_note
from violin_sound import generate_violin_note

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


class Instrument(Enum):
    BEAT = 0
    PIANO = 1
    VIOLIN = 2
    
def combine_notes_with_envelope(sequence: list[Note], sample_rate: int = SAMPLE_RATE, instrument: Instrument = Instrument.BEAT):
    combined_wave = np.array([])
    for note in sequence:
        if instrument == Instrument.BEAT:
            wave = generate_pulse_wave(note.get_frequency(), note.duration, sample_rate)
        elif instrument == Instrument.PIANO:
            wave = generate_piano_note(note.get_frequency(), note.duration, sample_rate)
        elif instrument == Instrument.VIOLIN:
            wave = generate_violin_note(note.get_frequency(), note.duration, sample_rate)
        combined_wave = np.concatenate((combined_wave, wave))
        
        # duration이 0.33 or 0.66 같은 triplet 일 경우 rest를 약간 추가해야 함
        if note.duration in [0.33 * NOTE_DURATION, 0.66 * NOTE_DURATION]:
            rest = generate_pulse_wave(0, note.duration * 0.3, sample_rate)
            combined_wave = np.concatenate((combined_wave, rest))
    return combined_wave

def play_sequence_with_envelope(sequence: list[Note], sample_rate: int = SAMPLE_RATE, instrument: Instrument = Instrument.BEAT):
    sd.play(combine_notes_with_envelope(sequence, sample_rate, instrument), sample_rate)
    sd.wait()