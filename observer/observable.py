import abc


class Observable(abc.ABC):

    def __init__(self):
        self._observers = []

    # If you override this method, I will find you and I will kill you.
    def register_observer(self, observer):
        self._observers.append(observer)

    # Same.
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)
