"""
This is a simple test script that tests the basic functionality of the timer class.
"""

from timer import Timer


def testfunc(t):
    print(".")

tim = Timer()
tim.init(mode=Timer.PERIODIC, period=500, callback=testfunc)
# timer.deinit()