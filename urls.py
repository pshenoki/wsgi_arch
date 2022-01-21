from page_controllers import IndexPage, FirePage, WaterPage, ContactPage
from front_controllers import TopFront, BottomFront

ROUTES = {
    '/': IndexPage(),
    '/fire': FirePage(),
    '/water': WaterPage(),
    '/contact': ContactPage()
}

FRONTS = [TopFront(), BottomFront()]
