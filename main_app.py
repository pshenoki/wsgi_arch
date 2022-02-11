from wsgi_framework.app import Application, ProxyLogApplication, ProxyFakeApplication
from urls import ROUTES, FRONTS
from sql_mapper import TableCreator
from config import CONNECTION

db_creator = TableCreator(CONNECTION).create_tables()

run_object = Application(routes=ROUTES, fronts=FRONTS)
# run_object = ProxyLogApplication(routes=ROUTES, fronts=FRONTS)
# run_object = ProxyFakeApplication(routes=ROUTES, fronts=FRONTS)


