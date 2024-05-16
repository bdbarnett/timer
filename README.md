# timer

A timer class for MicroPython on Unix and CPython that provides the same functionality and API as MicroPython's machine.Timer class on microcontrollers.  Will use MicroPython's machine.Timer if run on a microcontroller, so it may be used in all 3 scenarios.  Currently does not support CircuitPython.

Requires [sdl2_lib](https://github.com/bdbarnett/sdl2_lib) on CPython, which requires [SDL2](https://github.com/libsdl-org/SDL/tree/SDL2)

Usage is the same as MicroPython's timer, except use `from timer import Timer` instead of `from machine import Timer`:

```
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
```
