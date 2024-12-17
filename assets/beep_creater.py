import numpy as np
import soundfile as sf
import sounddevice as sd
# Constants for the NES sound system
SAMPLE_RATE = 44100  # Hz
DURATION = 1  # 1 second for each bar
AMPLITUDE = 0.5  # Amplitude of the wave

def generate_pulse_wave(frequency, duty_cycle=0.5, duration=1, sample_rate=44100):
    """Generate a pulse (square) wave with a given frequency and duty cycle."""
    t = np.arange(0, duration, 1 / sample_rate)
    pulse_wave = np.where(np.sin(2 * np.pi * frequency * t) > (1 - 2 * duty_cycle), 1, -1)
    return AMPLITUDE * pulse_wave

def generate_triangle_wave(frequency, duration=1, sample_rate=44100):
    """Generate a triangle wave with a given frequency."""
    t = np.arange(0, duration, 1 / sample_rate)
    triangle_wave = 2 * np.abs(2 * ((t * frequency) % 1) - 1) - 1
    return AMPLITUDE * triangle_wave

def generate_noise(duration=1, sample_rate=44100):
    """Generate white noise."""
    noise = np.random.uniform(-1, 1, int(sample_rate * duration))
    return AMPLITUDE * noise

def generate_dmc_sample(sample_data, sample_rate=44100):
    """Generate a DMC-like 1-bit delta-modulation-encoded waveform."""
    current_value = 0
    dmc_wave = []
    for sample in sample_data:
        if sample > current_value:
            current_value += 1
        else:
            current_value -= 1
        dmc_wave.append(current_value / 127)  # Normalize to -1 to 1 range
    return np.array(dmc_wave)

# 1. Generate Pulse 1 (C4 Note)
pulse_1_wave = generate_pulse_wave(frequency=261.63, duty_cycle=0.5, duration=DURATION, sample_rate=SAMPLE_RATE)

sf.write('pulse_1.wav', pulse_1_wave, SAMPLE_RATE)

# 2. Generate Pulse 2 (E4 Note)
pulse_2_wave = generate_pulse_wave(frequency=329.63, duty_cycle=0.75, duration=DURATION, sample_rate=SAMPLE_RATE)
sf.write('pulse_2.wav', pulse_2_wave, SAMPLE_RATE)

sd.play(pulse_2_wave)

# 3. Generate Triangle Wave (G3 Note)
triangle_wave = generate_triangle_wave(frequency=196.00, duration=DURATION, sample_rate=SAMPLE_RATE)
sf.write('triangle.wav', triangle_wave, SAMPLE_RATE)

# 4. Generate Noise (Percussion-like)
noise_wave = generate_noise(duration=DURATION, sample_rate=SAMPLE_RATE)
sf.write('noise.wav', noise_wave, SAMPLE_RATE)

# 5. Generate a DMC-like sample (voice sample simulation)
sample_data = np.random.randint(-127, 127, int(SAMPLE_RATE * DURATION))  # Random data for DMC
dmc_wave = generate_dmc_sample(sample_data, sample_rate=SAMPLE_RATE)
sf.write('dmc_sample.wav', dmc_wave, SAMPLE_RATE)

print("4 NES-style audio assets and 1 DMC-like sample have been created!")




