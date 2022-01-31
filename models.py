class Director:
    category_dict = {}

    @staticmethod
    def create_category(request):
        return CategoryModel(request)

    @classmethod
    def update_category_dict(cls, category_model):
        if category_model.category_name not in cls.category_dict:
            cls.category_dict[category_model.category_name] = category_model

    @classmethod
    def insert_curs_to_category(cls, curs):
        if curs.curs_cat in cls.category_dict:
            cls.category_dict[curs.curs_cat].insert_curs(curs)

    @staticmethod
    def create_curs(request):
        return CursFactory.create(request)


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

    def insert_curs(self, curs):
        self.curses.append(curs)


class CursModel:
    def __init__(self, request):
        self.request = request
        self._curs_name = request['curs_name']
        self._curs_cat = request['curs_cat']
        self.curs_type = request['curs_type']
        self.students = []

    def insert_curs_list(self, cat_list):
        cat_list.append(self)

    @property
    def curs_name(self):
        return self._curs_name

    @property
    def curs_cat(self):
        return self._curs_cat


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
