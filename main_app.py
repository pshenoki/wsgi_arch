from wsgi_framework.app import Application
from urls import ROUTES, FRONTS

run_object = Application(routes=ROUTES, fronts=FRONTS)
