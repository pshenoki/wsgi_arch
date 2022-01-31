from page_controllers import IndexPage, FirePage, WaterPage, ContactPage, \
    CreateCategory, CategoryList, CreateCurs
from front_controllers import TopFront, BottomFront

ROUTES = {
    '/': IndexPage(),
    '/fire': FirePage(),
    '/water': WaterPage(),
    '/contact': ContactPage(),
    '/createcat': CreateCategory(),
    '/categores': CategoryList(),
    '/createcurs': CreateCurs()
}

FRONTS = [TopFront(), BottomFront()]
