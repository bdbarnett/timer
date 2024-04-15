from ._timerbase import _TimerBase
import threading

class Timer(_TimerBase):

    def _start(self):
        self._thread = threading.Timer(self._interval, self._timer_callback)
        self._thread.start()

    def _stop(self):
        if self._thread:
            self._thread.cancel()
            self._thread = None

    def _timer_callback(self):
        super()._timer_callback()
        if self._mode == Timer.PERIODIC:
            self._start()  # threading.Timer is one-shot, so we need to restart it


