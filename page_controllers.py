from wsgi_framework.page_controllers import PageController
from wsgi_framework.shablonizator import render
from wsgi_framework.utils import save_to_file
from utils import info_we_need, debug
from models import Director, CategoryDirector, CursDirector
from sql_mapper import CategoryMapper, CursMapper, StudentMapper
from config import CONNECTION
import json

category_mapper = CategoryMapper(CONNECTION)
curs_mapper = CursMapper(CONNECTION)
student_mapper = StudentMapper(CONNECTION)


@debug
class IndexPage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='index.html',
                                say_me='MY HOME PAGE',
                                front_request=request).encode('UTF-8')


@debug
class ContactPage(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='contact.html',
                                    say_me='CONTACTS PAGE',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=info_we_need(request), filename='post_data.txt')
            return '200 OK', render(template_name='greeting.html',
                                    say_me='Поздравляю',
                                    front_request=request).encode('UTF-8')


@debug
class CreateCategory(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='create_category.html',
                                    say_me='Выберите название категории:',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=request, filename='post_data.txt')
            cat = Director.create_category(request)
            CategoryDirector.update(cat)

            category_mapper.create_category(request['cat_name'])
            return '200 OK', render(template_name='categores.html',
                                    object_list=CategoryDirector.category_dict,
                                    db_list=category_mapper.select_all(),
                                    say_me='Список доступных категорий и курсов:',
                                    front_request=request).encode('UTF-8')


class CategoryApi(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='category_api.html',
                                    say_me='Выберите название категории для получения информации,'
                                           ' для получения информации по всем категориям напишите "all":',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=request, filename='post_data.txt')
            memento = Director.create_memento_category(request)
            memento.memento_json()
            return '200 OK', render(template_name='memento_category.json',
                                    front_request=request).encode('UTF-8')


class CategoryList(PageController):
    def __call__(self, request):

        return '200 OK', render(template_name='categores.html',
                                object_list=CategoryDirector.category_dict,
                                db_list=category_mapper.select_all(),
                                db_list_curs=curs_mapper.select_all(),
                                db_list_stud='',
                                say_me='Список доступных категорий:',
                                front_request=request).encode('UTF-8')


class CreateCurs(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='create_curs.html',
                                    say_me='Выберите название курса:',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=request, filename='post_data.txt')
            curs = Director.create_curs(request)
            CategoryDirector.insert_curs_to_category(curs)

            curs_mapper.create_curs(request['curs_name'], request['curs_cat'], request['curs_type'])
            return '200 OK', render(template_name='categores.html',
                                    object_list=CategoryDirector.category_dict,
                                    db_list=category_mapper.select_all(),
                                    db_list_curs=curs_mapper.select_all(),
                                    db_list_stud='',
                                    say_me='Список доступных категорий и курсов:',
                                    front_request=request).encode('UTF-8')


class CreateStudent(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='create_student.html',
                                    say_me='Представьтесь и выберите курс:',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=request, filename='post_data.txt')
            student = Director.create_student(request)
            CursDirector.insert_student_to_students_list(student)

            student_mapper.create_student(request['lname'], request['fname'], request['email'])
            return '200 OK', render(template_name='id.html',
                                    object_list=(student.get_id(), student.all_students),
                                    db_list_stud=(student_mapper.select_all(),
                                                  student_mapper.return_id_by_name(request['lname'],
                                                                                   request['fname'])),
                                    say_me='Список доступных категорий и курсов:',
                                    front_request=request).encode('UTF-8')


class GoToCurs(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='go_to_curs.html',
                                    say_me='Представьтесь и выберите курс:',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=request, filename='post_data.txt')
            claim = Director.create_claim(request)
            CursDirector.insert_student_to_curs(curs=claim.find_curs(), student=claim.find_student())

            student_mapper.insert_student_to_curs(curs_mapper.select_curs_id_by_data(request['curs_cat'],
                                                                                     request['curs_name']),
                                                  request['student_id'])
            return '200 OK', render(template_name='categores.html',
                                    object_list=CategoryDirector.category_dict,
                                    say_me='Список доступных категорий и курсов:',
                                    front_request=request).encode('UTF-8')
