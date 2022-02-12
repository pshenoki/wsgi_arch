from utils import id_counter_gen


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
            if str(student.id) == str(st_id):
                return student

    def sign_up_on_curs(self, curs_name):
        curs_name.insert_student(self)

    def go_to_list(self):
        self.all_students.append(self)


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
