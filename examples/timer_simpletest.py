"""
This is a simple test script that tests the basic functionality of the timer class.
"""

from timer import Timer
try:
    from micropython import schedule
except ImportError:
    schedule = lambda f, x: f(x)


def testfunc(_):
    print(".")

def schedule_testfunc(t):
    schedule(testfunc, 0)

def cancel(_):
    print("Cancelling timer 1.")
    tim1.deinit()

def schedule_cancel(t):
    schedule(cancel, 0)

# Create a timer that prints a dot every 500ms
tim1 = Timer()
print("Starting timer 1.")
tim1.init(mode=Timer.PERIODIC, period=500, callback=schedule_testfunc)

# Create a timer that cancels the first timer after 5 seconds
tim2 = Timer()
tim2.init(mode=Timer.ONE_SHOT, period=5000, callback=schedule_cancel)
