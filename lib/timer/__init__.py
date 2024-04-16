"""
Universal Timer class for *Python.

Currently, only MicroPython is supported, but other platforms may be added in the future.
_sdl2.py is another implementation for MicroPython on Unix, but not currently working.
_sched.py is a reference implementation for CPython, but it is blocking as written.
_threading.py is a reference implementation for CPython, but it is not currently working.

The goal is to be able to use 'from timer import Timer' on MicroPython on microcontrollers,
on MicroPython on Unix (which doesn't have a machine.Timer) and CPython (ditto).

Although _ffi.py is working for MicroPython on Unix, _sdl2.py is a much simpler implementation,
if only it worked :).  _ffi.py uses uses MicroPython ffi to connect to libc and librt, while
_sdl2.py uses MicroPython ffi to connect to libSDL2-2.0.  Once _sdl2.py is working, we should
easily (fingers crossed) be able to port that to _sdl2_cpython.py and use cffi or ctypes for CPython.
At that point, we can then focus on compatibility under CircuitPython, then remove all unused
implementations like _sched.py and _threading.py.

Usage:
    from timer import Timer
    tim = Timer()
    tim.init(mode=Timer.Periodic, period=1, callback=lambda t: print(".", end=""))
    ....
    tim.deinit()
"""

try:
    from machine import Timer  # MicroPython on microcontrollers
except ImportError:
    import sys
    if sys.implementation.name == "micropython":  # MicroPython on Unix
        from ._ffi import Timer
    else:
        Timer = None
