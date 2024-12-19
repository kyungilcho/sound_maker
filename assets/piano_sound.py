import numpy as np
import matplotlib.pyplot as plt

attack_time = 0.01
release_time = 0.03
sustain_level = 0.4
decay_time = 0.1


def generate_piano_note(frequency, duration=2, sample_rate=44100):
    t = np.linspace(0, duration + attack_time + release_time, int(sample_rate * (duration + attack_time + release_time)), False)

    # Fundamental frequency
    signal = np.sin(2 * np.pi * frequency * t)
    
    if frequency == 0:
        return np.zeros_like(t)

    # Add harmonics
    for i in range(1, 15):
        signal += (0.5) ** i * np.sin(2 * np.pi * frequency * i * t)

    # # Apply ADSR envelope
    envelope = adsr_envelope(t,attack_time=attack_time, decay_time=decay_time, sustain_level=sustain_level, release_time=release_time, duration=duration)
    
    # draw_two_dimensional_graph(t, envelope, "ADSR Envelope", "Time (s)", "Amplitude")
    
    # piano_note = signal
    
    piano_note = signal * envelope
    

    # Normalize to prevent clipping
    piano_note = piano_note / np.max(np.abs(piano_note))

    return piano_note


def adsr_envelope(t,attack_time, decay_time, sustain_level, release_time, duration):
    """
    Generate an ADSR envelope.

    Parameters:
    - t: Time array
    - attack time: Attack time in seconds (it should be 0.01 by default)
    - decay_time: Decay time in seconds
    - sustain_level: Sustain amplitude (0 to 1), 1 is equal to the maximum amplitude(attack)
    - release: Release time in seconds
    - duration: Total duration in seconds

    Returns:
    - Envelope array
    """
    # envelope = np.zeros_like(t)
    # for i, time in enumerate(t):
    #     if time < attack_time:
    #         envelope[i] = time / attack_time
    #     elif time < duration - (sustain_time * duration + release_time):
    #         envelope[i] = (sustain_level - 1) / (duration - duration * sustain_time - release_time - attack_time) * time + 1 - ((sustain_level - 1) / (duration - duration * sustain_time - release_time - attack_time) * attack_time)
    #     elif time < duration - release_time:
    #         envelope[i] = sustain_level
    #     elif time < duration:
    #         envelope[i] = sustain_level * (1 - (time - (duration - release_time)) / release_time)
    #     else:
    #         envelope[i] = 0
    # return envelope
    envelope = np.zeros_like(t)
    for i, time in enumerate(t):
        if time < attack_time:
            envelope[i] = time / attack_time
        elif time < decay_time + attack_time:
            envelope[i] = (sustain_level - 1) / (decay_time) * time + 1 - ((sustain_level - 1) / (decay_time) * attack_time)
        elif time < duration + attack_time:
            envelope[i] = sustain_level
        elif time < duration + release_time + attack_time:
            envelope[i] = - sustain_level / release_time * time  + sustain_level * (duration + attack_time + release_time) / release_time
        else:
            envelope[i] = 0
    return envelope

def draw_two_dimensional_graph(x, y, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# # Generate and play a C4 note (~261.63 Hz)
# c4_freq = 261.63
# note = generate_piano_note(Note("C5").get_frequency(), duration= 1/6)
# sd.play(note, 44100)
# sd.wait()

# beep = generate_pulse_wave(c4_freq, duration=1)
# sd.play(beep, 44100)
# sd.wait()