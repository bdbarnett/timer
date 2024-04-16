"""
This script is NOT working.  See the comments below.
"""
from ._timerbase import _TimerBase
import ffi

SDL_INIT_TIMER = 1

_sdl = ffi.open("libSDL2-2.0.so.0")

SDL_Init = _sdl.func("i", "SDL_Init", "I")
SDL_AddTimer = _sdl.func("p", "SDL_AddTimer", "iCp")  # Not sure if this line is correct
SDL_RemoveTimer = _sdl.func("v", "SDL_RemoveTimer", "p")

class Timer(_TimerBase):
    def _start(self):
        SDL_Init(SDL_INIT_TIMER)
        cb = ffi.callback("v", self._timer_callback, "i", lock=True)  # Not sure if this line is correct
        self._timer = SDL_AddTimer(int(self._interval), cb.cfun(), self.id)  # Not sure if this line is correct

    def _stop(self):
        if self._timer:
            SDL_RemoveTimer(self._timer)
            self._timer = None
