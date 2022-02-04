from wsgi_framework.app import Application, ProxyLogApplication, ProxyFakeApplication
from urls import ROUTES, FRONTS

run_object = Application(routes=ROUTES, fronts=FRONTS)
# run_object = ProxyLogApplication(routes=ROUTES, fronts=FRONTS)
# run_object = ProxyFakeApplication(routes=ROUTES, fronts=FRONTS)
