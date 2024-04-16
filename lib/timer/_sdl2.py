"""
This script is NOT working.  See the comments below.

SDL2Display in MPDisplay uses ffi just like the implementation below, and is working completely.  However,
it does not use callbacks in any of it's ffi functions, so it is only a partially usefull example.  See:

https://pycopy.readthedocs.io/en/latest/library/ffi.html
https://wiki.libsdl.org/SDL2/SDL_AddTimer

Once this is working for MicroPython on Unix, we can create another implementation for CPython using 
"""
from ._timerbase import _TimerBase
try:
    import ffi

    SDL_INIT_TIMER = 1

    _sdl = ffi.open("libSDL2-2.0.so.0")

    SDL_Init = _sdl.func("i", "SDL_Init", "I")
    SDL_AddTimer = _sdl.func("p", "SDL_AddTimer", "iCp")  # Not sure if this line is correct
    SDL_RemoveTimer = _sdl.func("v", "SDL_RemoveTimer", "p")

    def SDL_TimerCallback(func):
        return (ffi.callback("v", func, "i", lock=True)).func()
except:
    from sdl2 import SDL_INIT_TIMER, SDL_Init, SDL_AddTimer, SDL_RemoveTimer, SDL_TimerCallback

class Timer(_TimerBase):
    def _start(self):
        SDL_Init(SDL_INIT_TIMER)
        cb = SDL_TimerCallback(self._callback)
        self._timer = SDL_AddTimer(int(self._interval), cb, self.id)

    def _stop(self):
        if self._timer:
            SDL_RemoveTimer(self._timer)
            self._timer = None
