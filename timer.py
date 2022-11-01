import time

class Timer:
    """Own timer class
    """    
    def __init__(self):
        """Creates a null start time to avoid issues
        """        
        self.starttime = None

    def start(self):
        """Starts timer at current time
        """        
        self.starttime = time.perf_counter()
        
    def getTime(self):
        """Get the time since the timer has started

        Returns:
            double: Time since the timer has started in seconds
        """        
        timepassed = time.perf_counter() - self.starttime
        return timepassed