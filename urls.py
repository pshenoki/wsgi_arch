from page_controllers import IndexPage, ContactPage, CreateCategory, CategoryList, CreateCurs
from front_controllers import TopFront, BottomFront

ROUTES = {
    '/': IndexPage(),
    '/contact': ContactPage(),
    '/createcat': CreateCategory(),
    '/categores': CategoryList(),
    '/createcurs': CreateCurs()
}

FRONTS = [TopFront(), BottomFront()]
