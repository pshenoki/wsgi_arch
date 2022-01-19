from wsgi_framework.app import Application
from page_controllers import IndexPage, FirePage, WaterPage
from front_controllers import TopFront, BottomFront


ROUTES = {
    '/': IndexPage(),
    '/fire': FirePage(),
    '/water': WaterPage(),
}

FRONTS = [TopFront(), BottomFront()]

run_object = Application(routes=ROUTES, fronts=FRONTS)
