from abc import ABC, abstractmethod


class PageController(ABC):
    @abstractmethod
    def __call__(self, request):
        pass


class NotFoundPage(PageController):
    def __call__(self, request):
        return '404 Not Found', b'404 page not found'

