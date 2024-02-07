from abc import ABCMeta,abstractmethod


class ICalcGeo(metaclass=ABCMeta):

    @property
    @abstractmethod
    def surface(self):
        pass