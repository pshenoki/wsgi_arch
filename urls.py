from page_controllers import IndexPage, FirePage, WaterPage, ContactPage, CreateCategory, CategoryList, CreateCurs, CursList
from front_controllers import TopFront, BottomFront

ROUTES = {
    '/': IndexPage(),
    '/fire': FirePage(),
    '/water': WaterPage(),
    '/contact': ContactPage(),
    '/createcat': CreateCategory(),
    '/categores': CategoryList(),
    '/createcurs': CreateCurs(),
    '/curses': CursList()
}

FRONTS = [TopFront(), BottomFront()]
