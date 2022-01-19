from abc import ABC, abstractmethod


class FrontController(ABC):
    @abstractmethod
    def __call__(self, request):
        pass
