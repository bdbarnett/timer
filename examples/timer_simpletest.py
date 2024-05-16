"""
This is a simple test script that tests the basic functionality of the timer class.
"""

from timer import Timer


def testfunc(t):
    print(".")

def cancel(t):
    print("Cancelling timer 1.")
    tim1.deinit()

# Create a timer that prints a dot every 500ms
tim1 = Timer()
print("Starting timer 1.")
tim1.init(mode=Timer.PERIODIC, period=500, callback=testfunc)

# Create a timer that cancels the first timer after 5 seconds
tim2 = Timer()
tim2.init(mode=Timer.ONE_SHOT, period=5000, callback=cancel)
