from wsgi_framework.page_controllers import NotFoundPage
from wsgi_framework.utils import check_slash
from wsgi_framework.utils import get_wsgi_input_data, parse_wsgi_input_data, save_to_file


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = check_slash(environ['PATH_INFO'])
        request = {}
        for front in self.fronts:
            front(request)

        if environ['REQUEST_METHOD'] == 'POST':
            # получаем данные
            input_data = get_wsgi_input_data(environ)
            # превращаем данные в словарь
            data = parse_wsgi_input_data(input_data)
            save_to_file(data)
            request.update(data)

        if path in self.routes:
            controller = self.routes[path]
        else:
            controller = NotFoundPage()
        code, body = controller(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [body]

