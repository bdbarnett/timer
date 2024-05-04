# SPDX-FileCopyrightText: 2024 Brad Barnett
#
# SPDX-License-Identifier: MIT
"""
Universal Timer class for *Python.

Enables using 'from timer import Timer' on MicroPython on microcontrollers,
on MicroPython on Unix (which doesn't have a machine.Timer) and CPython (ditto).

Although _ffi.py is working for MicroPython on Unix, _sdl2.py is a much simpler implementation,
if only the ffi implementation worked :).  _ffi.py uses uses MicroPython ffi to connect to libc
and librt, while _sdl2.py uses MicroPython ffi on Unix to connect to libSDL2-2.0 (not working)
OR py-sdl2 on CPython to connect to libSDL2 (working).  In the future, may be able to use cffi
or ctypes for CPython instead of py-sdl2.  No compatibility for CircuitPython yet.

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
    elif sys.implementation.name == "cpython":
        from ._sdl2 import Timer
    else:
        Timer = None
