import time, threading, queue

class Sonifier(threading.Thread):

    def __init__(self):
        super(Sonifier, self).__init__()
        self.daemon = True
        self.queue = queue.Queue()

    def add(self, f, delay):
        self.queue.put([time.perf_counter() + delay, f])

    def run(self):
        while True:
            remaining_tasks = []
            try:
                while True:
                    task = self.queue.get_nowait()
                    if task[0] <= time.perf_counter():
                        task[1]()
                    else:
                        remaining_tasks.append(task)
            except queue.Empty:
                pass
            for task in remaining_tasks:
                self.queue.put(task)
            time.sleep(1/60)

    def clear(self):
        try:
            while True:
                self.queue.get_nowait()
        except queue.Empty:
            pass
