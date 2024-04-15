from ._timerbase import _TimerBase
import sched

class Timer(_TimerBase):

    def init(self, **kwargs):
        self._scheduler = sched.scheduler()
        super().init(**kwargs)

    def _start(self):
        self._event = self._scheduler.enter(self._interval / 1000, 1, self._timer_callback)
        self._scheduler.run(blocking=True)

    def _stop(self):
        if self._event:
            self._scheduler.cancel(self._event)
            self._event = None
        self._scheduler = None

    def _timer_callback(self):
        super()._timer_callback()
        if self._mode == Timer.PERIODIC:
            self._start()  # sched.scheduler is one-shot, so we need to restart it
