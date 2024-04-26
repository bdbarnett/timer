from ._timerbase import _TimerBase
import sched

class Timer(_TimerBase):

    def init(self, **kwargs):
        self._scheduler = sched.scheduler()
        super().init(**kwargs)

    def _start(self):
        self._event = self._scheduler.enter(self._interval / 1000, 1, self._handler)
        self._scheduler.run(blocking=True)

    def _stop(self):
        if self._event:
            self._scheduler.cancel(self._event)
            self._event = None
        self._scheduler = None

    def _handler(self):
        ret = super()._handler()
        if ret:  # ret is 0 if the timer is one-shot
            self._start()  # sched.scheduler is one-shot, so we need to restart it
