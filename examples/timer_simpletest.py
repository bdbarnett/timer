"""
This is a simple test script that tests the basic functionality of the timer class.

It creates a periodic timer in a class instance and a one-shot timer that stops the periodic timer.
"""

from timer import Timer


class TimerTest:
    def __init__(self):
        self._tim = Timer(1)

    def start(self, period):
        self._counter = 0
        self._tim.init(mode=Timer.PERIODIC, period=period, callback=self.do_something)
        print("TimerTest:  timer started...")

    def do_something(self, t):
        self._counter += 1

    def stop(self, t=None):
        self._tim.deinit()
        print(f"TimerTest:  timer stopped after {self._counter:,} calls.")

# Create a timer that calls tt.do_something every 1ms
tt = TimerTest()
tt.start(1)  

# Create a timer that stops the first timer after 5 seconds
tim2 = Timer(2)
tim2.init(mode=Timer.ONE_SHOT, period=5000, callback=tt.stop)
