from braid import *

t1 = Thread(10)
t1.chord = C, DOR  # root note is "Hi Wood Block"

t2 = Thread(11)
t2.chord = C, DOR  # root note is "Lo Wood Block"

t1.pattern = [1., 2, R, 0], [1, R, 0, 1.], [0, 3, 1, 0]   # thanks Steve
t2.pattern = t1.pattern

t1.start()
t2.start(t1)            # t1 as argument

# t = Thread(1)               # create a thread with MIDI channel
# t.chord = C, DOR
# t.pattern = R, [1., R], 1, [3, 4., 3.] # we like this one!

# t.start()                   # start it
t2.phase = 6/12
play()                      # don't forget this
