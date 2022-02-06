import json
from utils import id_counter_gen


class Director:
    category_dict = {}

    @staticmethod
    def create_category(request):
        return CategoryModel(request)

    @staticmethod
    def create_curs(request):
        return CursFactory.create(request)

    @staticmethod
    def create_student(request):
        return StudentModel(request)

    @staticmethod
    def create_claim(request):
        return CursClaim(request)

    @staticmethod
    def create_memento_category(request):
        return MementoCategory(request)


class CategoryDirector:
    category_dict = {}

    @classmethod
    def update(cls, category_model):
        if category_model.category_name not in cls.category_dict:
            cls.category_dict[category_model.category_name] = category_model

    @classmethod
    def insert_curs_to_category(cls, curs):
        if curs.curs_cat in cls.category_dict:
            cls.category_dict[curs.curs_cat].insert_curs(curs)

    @classmethod
    def memento_category_json(cls, cat_name):
        data = []
        if cat_name == 'all':
            for c_name in cls.category_dict:
                curs_list = cls.category_dict[c_name].curses
                data.append({c_name: [curs.curs_name for curs in curs_list]})
        else:
            curs_list = cls.category_dict[cat_name].curses
            data = {cat_name: [curs.curs_name for curs in curs_list]}

        with open('templates/memento_category.json', 'w') as outfile:
            json.dump(data, outfile)

    @classmethod
    def return_curs_by_name(cls, category_name, curs_name_):
        curs_list = cls.category_dict[category_name].curses
        for curs in curs_list:
            if curs.curs_name == curs_name_:
                return curs


class MementoCategory:
    def __init__(self, request):
        self.request = request
        self.cat_name = request['cat_name']

    def memento_json(self):
        return CategoryDirector.memento_category_json(self.cat_name)


class CursDirector:

    @staticmethod
    def insert_student_to_curs(curs, student):
        if student.id not in [stud.id for stud in curs.students_list]:
            curs.students_list.append(student)

    @staticmethod
    def insert_student_to_students_list(student):
        student.go_to_list()


class StudentModel:

    id_counter = id_counter_gen()
    all_students = []

    def __init__(self, request):
        self.request = request
        self.fname = request['fname']
        self.lname = request['lname']
        self.email = request['email']
        self.id = next(self.id_counter)

    def get_id(self):
        return self.id

    @classmethod
    def return_student_by_id(cls, st_id):
        for student in cls.all_students:
            print(student.id, st_id)
            if str(student.id) == str(st_id):
                return student

    def sign_up_on_curs(self, curs_name):
        curs_name.insert_student(self)

    def go_to_list(self):
        self.all_students.append(self)


class CursClaim:
    def __init__(self, request):
        self.request = request
        self.category_name = request['curs_cat']
        self.curs_name = request['curs_name']
        self.student_id = request['student_id']

    def find_curs(self):
        return CategoryDirector.return_curs_by_name(category_name=self.category_name, curs_name_=self.curs_name)

    def find_student(self):
        return StudentModel.return_student_by_id(self.student_id)


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
        self.students_list = []

    def insert_curs_list(self, cat_list):
        cat_list.append(self)

    @property
    def curs_name(self):
        return self._curs_name

    @property
    def curs_cat(self):
        return self._curs_cat

    def insert_student(self, student):
        self.students_list.append(student)


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
