import gzip, pickle
import numpy as np

def save(data, filename):
    with gzip.open(filename, 'wb') as f:
        f.write(pickle.dumps(data))

def load(filename):
    with gzip.open(filename) as f:
        data = pickle.loads(f.read())
    return data

def normalize(signal, minimum=None, maximum=None):
    """Normalize a signal to the range 0, 1. Uses the minimum and maximum observed in the data unless explicitly passed."""
    signal = np.array(signal).astype('float')
    if minimum is None:
        minimum = np.min(signal)
    if maximum is None:
        maximum = np.max(signal)
    signal -= minimum
    maximum -= minimum
    signal /= maximum
    signal = np.clip(signal, 0.0, 1.0)
    return signal

def rescale(v, in_min, in_max, out_min, out_max):
    return (((v - in_min) / (in_max - in_min)) * (out_max - out_min)) + out_min

def clip(v, min_v, max_v):
    return min(max(v, min_v), max_v)
