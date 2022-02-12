from model.director_model import CategoryDirector
from model.main_model import StudentModel


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


class MementoCategory:
    def __init__(self, request):
        self.request = request
        self.cat_name = request['cat_name']

    def memento_json(self):
        return CategoryDirector.memento_category_json(self.cat_name)