# SPDX-FileCopyrightText: 2024 Brad Barnett
#
# SPDX-License-Identifier: MIT
"""
Timer using sdl2_lib with the same API as machine.Timer in MicroPython
"""
from ._timerbase import _TimerBase

try:
    from sdl2_lib import SDL_INIT_TIMER, SDL_Init, SDL_AddTimer, SDL_RemoveTimer, SDL_TimerCallback
except ImportError:
    raise ImportError("SDL2 library not found")


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