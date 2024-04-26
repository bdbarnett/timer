from ._timerbase import _TimerBase
import threading

class Timer(_TimerBase):

    def init(self, **kwargs):
        self._thread = threading.Timer(self._interval, self._handler)
        super().init(**kwargs)

    def _start(self):
        self._thread.start()

    def _stop(self):
        if self._thread:
            self._thread.cancel()
            self._thread = None

    def _handler(self):
        super()._handler()
        if self._mode == Timer.PERIODIC:
            self._start()  # threading.Timer is one-shot, so we need to restart it


