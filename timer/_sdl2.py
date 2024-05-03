# SPDX-FileCopyrightText: 2024 Brad Barnett
#
# SPDX-License-Identifier: MIT
"""
Timer using SDL2 with the same API as machine.Timer in MicroPython

The ffi implementation isn't working quite right, but the py-sdl2
implementation is working fine.
"""
from ._timerbase import _TimerBase

try:
    import ffi  # See https://pycopy.readthedocs.io/en/latest/library/ffi.html

    SDL_INIT_TIMER = 1

    _sdl = ffi.open("libSDL2-2.0.so.0")

    SDL_Init = _sdl.func("i", "SDL_Init", "I")
    SDL_AddTimer = _sdl.func("P", "SDL_AddTimer", "ICP")  # Not sure if this line is correct
    SDL_RemoveTimer = _sdl.func("v", "SDL_RemoveTimer", "P")

    def SDL_TimerCallback(tcb):
        return (ffi.callback("I", tcb, "IP", lock=True)).cfun()
except ImportError:
    try:
        from sdl2 import SDL_INIT_TIMER, SDL_Init, SDL_AddTimer, SDL_RemoveTimer, SDL_TimerCallback
    except ImportError:
        raise ImportError("Install the py-sdl2 package using 'pip install pysdl2' and possibly 'pip install pysdl2-dll'")



class Timer(_TimerBase):
    def _start(self):
        SDL_Init(SDL_INIT_TIMER)
        self._handler_ref = self._handler
        self._tcb = SDL_TimerCallback(self._handler_ref)
        self._timer = SDL_AddTimer(self._interval, self._tcb, None)

    def _stop(self):
        if self._timer:
            SDL_RemoveTimer(self._timer)
            self._timer = None
            self._tcb = None
            self._handler_ref = None