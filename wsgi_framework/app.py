from wsgi_framework.page_controllers import NotFoundPage
from wsgi_framework.utils import check_slash


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = check_slash(environ['PATH_INFO'])
        request = {}
        for front in self.fronts:
            front(request)

        if path in self.routes:
            controller = self.routes[path]
        else:
            controller = NotFoundPage()
        code, body = controller(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [body]

