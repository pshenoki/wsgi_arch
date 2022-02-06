from page_controllers import IndexPage, ContactPage, CreateCategory, CategoryList,\
    CreateCurs, CreateStudent, GoToCurs, CategoryApi
from front_controllers import TopFront, BottomFront

ROUTES = {
    '/': IndexPage(),
    '/contact': ContactPage(),
    '/createcat': CreateCategory(),
    '/categores': CategoryList(),
    '/createcurs': CreateCurs(),
    '/createstudent': CreateStudent(),
    '/gotocurs': GoToCurs(),
    '/categoryapi': CategoryApi(),
}

FRONTS = [TopFront(), BottomFront()]
