#!/usr/bin/env python3

import threading, queue
from pythonosc.udp_client import SimpleUDPClient


class OSCOut(threading.Thread):

    def __init__(self, port=0, throttle=0):
        print("Starting OSC...")
        threading.Thread.__init__(self)
        self.daemon = True
        self.port = port
        self.throttle = throttle
        self.queue = queue.Queue()
        self.osc = SimpleUDPClient("127.0.0.1", port)
        self.log_osc = False
        self.start()

    def send(self, address, message):
        self.queue.put((address, message))

    def run(self):
        while True:
            address, message = self.queue.get()
            if self.log_osc:
                print(f"OSC {address} {message}")
            self.osc.send_message(address, message)
            if self.throttle > 0:
                time.sleep(self.throttle)

# osc_out = OSCOut(5005)
