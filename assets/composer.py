import soundfile as sf

def adjust_wave(wave, sample_rate, volume):
    return wave * volume

def compose_wave(wave1, wave2, wave3, wave4, wave5, wave6, wave7, wave8, wave9, wave10):
    return wave1 + wave2 + wave3 + wave4 + wave5 + wave6 + wave7 + wave8 + wave9 + wave10


if __name__ == "__main__":
    wave1, sample_rate = sf.read("pulse_1.wav")
    wave2, sample_rate = sf.read("pulse_2.wav")
    wave3, sample_rate = sf.read("triangle.wav")
    wave4, sample_rate = sf.read("dmc_sample.wav")
    wave5, sample_rate = sf.read("noise.wav")

    composed_wave = compose_wave(wave1, wave2, wave3, wave4, wave5, wave1, wave2, wave3, wave4, wave5)
    sf.write("composed_wave.wav", composed_wave, sample_rate)
    
