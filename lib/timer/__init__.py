"""
Universal Timer class for *Python.

Currently, only MicroPython is supported, but other platforms may be added in the future.
_sdl2.py is another implementation for MicroPython on Unix, but not currently working.
_sched.py is an implementation for CPython, but it is blocking as written.
_threading.py is an implementation for CPython, but it is not currently working.
"""

try:
    from machine import Timer  # MicroPython on microcontrollers
except ImportError:
    import sys
    if sys.implementation.name == "micropython":  # MicroPython on Unix
        from ._ffi import Timer
    else:
        Timer = None