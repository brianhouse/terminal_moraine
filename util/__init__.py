import math
from util.midi import midi_out

midi_out.log_midi = True

def get_point(start_point, angle, distance):
    x, y = start_point
    return x + (distance * math.cos(math.radians(angle))), y + (distance * math.sin(math.radians(angle)))
