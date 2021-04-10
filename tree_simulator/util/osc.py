#!/usr/bin/env python3

import threading, queue
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.dispatcher import Dispatcher


class OSCOut(threading.Thread):

    def __init__(self, port, throttle=0):
        print("Starting OSCOut...")
        threading.Thread.__init__(self)
        self.daemon = True
        self.port = port
        self.throttle = throttle
        self.queue = queue.Queue()
        self.osc = SimpleUDPClient("127.0.0.1", self.port)
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


class OSCIn(threading.Thread):

    def __init__(self, port, callback):
        print("Starting OSCIn...")
        threading.Thread.__init__(self)
        self.daemon = True
        self.port = port
        dispatcher = Dispatcher()
        dispatcher.set_default_handler(callback)
        self.osc = BlockingOSCUDPServer(("127.0.0.1", self.port), dispatcher)
        self.log_osc = False
        self.callback = callback
        self.start()

    def run(self):
        print("running...")
        self.osc.serve_forever()
