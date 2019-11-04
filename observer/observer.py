import abc


class Observer(abc.ABC):

    @abc.abstractmethod
    def notify(self, observable, *args, **kwargs):
        pass
