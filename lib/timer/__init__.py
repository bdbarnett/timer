"""
Universal Timer class for *Python - The goal is to have a single Timer class that works on all Python platforms.

Uses machine.Timer on MicroPython on microcontrollers.
_ffi.py is an implementation for MicroPython on Unix.
_sdl2.py is an implementation for CPython.
_sched.py and _threading.py are partially working yet unused implementations for reference only.

Although _ffi.py is working for MicroPython on Unix, _sdl2.py is a much simpler implementation.
_ffi.py uses uses MicroPython ffi to connect to libc and librt.

_sdl2.py currently works for CPython, but it depends on py-sdl2 via:
    'pip install pysdl2' for all CPython platforms.
    'pip install pysdl2-dll' for Windows.
It should be possible to use cffi or ctypes for CPython instead of depending on py-sdl2.

_sdl2.py has NON-WORKING code to use ffi on MicroPython to connect to libSDL2-2.0.

A timer for CircuitPython has not been implemented yet.  Once it is, we should remove all unused
implementations like _sched.py and _threading.py.
"""

try:
    from machine import Timer  # MicroPython on microcontrollers
except ImportError:
    import sys
    if sys.implementation.name == "micropython":  # MicroPython on Unix
        from ._ffi import Timer
    elif sys.implementation.name == "cpython":  # CPython
        from ._sdl2 import Timer
    else:
        Timer = None
