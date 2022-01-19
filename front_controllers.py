from wsgi_framework.front_controllers import FrontController


class TopFront(FrontController):
    def __call__(self, request):
        request['top_page'] = 'Привет, я фронт контроллер с заголовком страницы'


class BottomFront(FrontController):
    def __call__(self, request):
        request['bottom_page'] = 'Привет, я фронт контроллер с подвалом страницы'
