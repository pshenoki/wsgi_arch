category_list = []
curs_list = []


class CategoryModel:
    def __init__(self, request):
        self.request = request
        self.cat_name = request['cat_name']
        self.curses = []

    def insert_cat_list(self, cat_list):
        if self.cat_name in [cat.category_name for cat in cat_list]:
            pass
        else:
            cat_list.append(self)

    @property
    def category_name(self):
        return self.cat_name


class CursModel:
    def __init__(self, request):
        self.request = request
        self.curs_name = request['curs_name']
        self.curs_type = request['curs_type']
        self.students = []

    def insert_curs_list(self, cat_list):
        cat_list.append(self)

    @property
    def category_name(self):
        return self.curs_name


class OnlineCurs(CursModel):
    pass


class OfflineCurs(CursModel):
    pass


class CursFactory:
    type_dict = {
        'online': OnlineCurs,
        'offline': OfflineCurs
    }

    @classmethod
    def create(cls, request):
        if request['curs_type'] in cls.type_dict:
            return cls.type_dict[request['curs_type']](request)
