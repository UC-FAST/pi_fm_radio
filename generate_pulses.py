#!/usr/bin/python



import scipy.io.wavfile as wavfile
import numpy

sample_rate = 228000
samples = numpy.zeros(2 * sample_rate, dtype=numpy.dtype('>i2'))

# 1-second tune
samples[:sample_rate] = (numpy.sin(2*numpy.pi*440*numpy.arange(sample_rate)/sample_rate)
        * 20000).astype(numpy.dtype('>i2'))

wavfile.write("pulses.wav", sample_rate, samples)
