"""
This script is NOT working.  See the comments below.

SDL2Display in MPDisplay uses ffi and is working completely.  However, it does not use callbacks in any of its
ffi functions, so it is only a partially usefull example.  See:

https://pycopy.readthedocs.io/en/latest/library/ffi.html
https://wiki.libsdl.org/SDL2/SDL_AddTimer

Once this is working for MicroPython on Unix, we can create another implementation for CPython.


This works:

import sdl2
def timerfunc(interval, param):
    print(".")
    return interval
sdl2.SDL_Init(sdl2.SDL_INIT_TIMER)
callback = sdl2.SDL_TimerCallback(timerfunc)
timerid = sdl2.SDL_AddTimer(1, callback, "Test")
# sdl2.SDL_RemoveTimer(timerid)


This segfaults unless using CPython / pysdl2 with cb = SDL_TimerCallback(self._callback) instead of cb = SDL_TimerCallback(self._timer_callback):

from timer._sdl2 import Timer
def timerfunc(interval, param):
    print(".")
    return interval
tim = Timer()
tim.Init(mode=Timer.PERIODIC, period=1, callback=timerfunc)
# timer.deinit()

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
