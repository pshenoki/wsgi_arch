from model.main_model import CategoryModel, StudentModel, CursFactory
from model.connectors import MementoCategory, CursClaim


class Director:

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