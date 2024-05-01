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
    import ffi  # succeeds if running MicroPyton under Unix

    SDL_INIT_TIMER = 1

    _sdl = ffi.open("libSDL2-2.0.so.0")

    SDL_Init = _sdl.func("i", "SDL_Init", "I")
    SDL_AddTimer = _sdl.func("p", "SDL_AddTimer", "iCp")  # Not sure if this line is correct
    SDL_RemoveTimer = _sdl.func("v", "SDL_RemoveTimer", "p")

    def SDL_TimerCallback(func):
        return (ffi.callback("v", func, "i", lock=True)).func()
except:
    # Running CPython.  Must install https://github.com/py-sdl/py-sdl2/ with 'pip install pysdl2' and possibly 'pip install pysdl2-dll'
    from sdl2 import SDL_INIT_TIMER, SDL_Init, SDL_AddTimer, SDL_RemoveTimer, SDL_TimerCallback

class Timer(_TimerBase):
    def _start(self):
        SDL_Init(SDL_INIT_TIMER)
        cb = SDL_TimerCallback(self._timer_callback)
        self._timer = SDL_AddTimer(int(self._interval), cb, self.id)

    def _stop(self):
        if self._timer:
            SDL_RemoveTimer(self._timer)
            self._timer = None
