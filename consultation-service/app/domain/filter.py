from abc import ABCMeta, abstractmethod


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def apply(self) -> bool:
        pass
