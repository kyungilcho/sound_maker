import numpy as np
import matplotlib.pyplot as plt
from piano_sound import adsr_envelope

attack_time = 0.05
release_time = 0.03
sustain_level = 0.5
decay_time = 0.12


def generate_violin_note(frequency, duration=2, sample_rate=44100):
    t = np.linspace(0, duration + attack_time + release_time, int(sample_rate * (duration + attack_time + release_time)), False)

    # Fundamental frequency
    signal = np.sin(2 * np.pi * frequency * t)
    
    if frequency == 0:
        return np.zeros_like(t)

    # Add harmonics
    signal += (0.94) * np.cos(2 * np.pi * frequency * 2 * t)
    signal += (0.425) * np.sin(2 * np.pi * frequency * 3 * t)
    signal += (0.48) * np.cos(2 * np.pi * frequency * 4 * t)
    signal += (0.365) * np.cos(2 * np.pi * frequency * 6 * t)
    signal += (0.04) * np.sin(2 * np.pi * frequency * 7 * t)
    signal += (0.085) * np.cos(2 * np.pi * frequency * 8 * t)
    signal += (0.090) * np.cos(2 * np.pi * frequency * 10 * t)

    # Apply ADSR envelope
    envelope = adsr_envelope(t,attack_time=attack_time, decay_time=decay_time, sustain_level=sustain_level, release_time=release_time, duration=duration)
    
    # draw_two_dimensional_graph(t, envelope, "ADSR Envelope", "Time (s)", "Amplitude")
    
    violin_note = signal * envelope

    # Normalize to prevent clipping
    violin_note = violin_note / np.max(np.abs(violin_note))

    return violin_note