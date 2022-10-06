import time

class Timer:
    def __init__(self):
        self.starttime = None

    def start(self):
        self.starttime = time.perf_counter()
        
    def getTime(self):
        timepassed = time.perf_counter() - self.starttime
        return timepassed