import numpy as np
import colorednoise as cn


def create_signal(sample_rate, time_of_signal, pad_samples, signal_type, voltage_out):
    number_of_samples = int(time_of_signal*sample_rate)
    if signal_type == "pink_noise":
        signal_unpadded = cn.powerlaw_psd_gaussian(1, number_of_samples)
    elif signal_type == "white_noise":
        signal_unpadded = cn.powerlaw_psd_gaussian(0, number_of_samples)
    elif signal_type == "debug":
        signal_unpadded = np.sin(34 * 2 * np.pi * np.linspace(0, time_of_signal, number_of_samples))
    signal_unpadded /= (np.max(abs(signal_unpadded)))/voltage_out
    signal = np.pad(signal_unpadded, (pad_samples, 0), 'constant', constant_values=[0, 0])

    return signal, signal_unpadded
