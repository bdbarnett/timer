from ._timerbase import _TimerBase
import ffi
from micropython import const

SDL_INIT_TIMER = const(0x00000001)

_sdl = ffi.open("libSDL2-2.0.so.0")

SDL_Init = _sdl.func("i", "SDL_Init", "I")
SDL_AddTimer = _sdl.func("p", "SDL_AddTimer", "iCp")
SDL_RemoveTimer = _sdl.func("v", "SDL_RemoveTimer", "p")

class Timer(_TimerBase):
    def _start(self):
        SDL_Init(SDL_INIT_TIMER)
        cb = ffi.callback("v", self._callback, "i", lock=True)
        self._timer = SDL_AddTimer(int(self._interval), cb.cfun(), self.id)

    def _stop(self):
        if self._timer:
            SDL_RemoveTimer(self._timer)
            self._timer = None
