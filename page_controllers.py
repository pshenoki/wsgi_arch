from wsgi_framework.page_controllers import PageController
from wsgi_framework.shablonizator import render
from wsgi_framework.utils import save_to_file
from utils import info_we_need
from models import category_list, CategoryModel, curs_list, CursFactory


class IndexPage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='index.html',
                                say_me='MY HOME PAGE',
                                front_request=request).encode('UTF-8')


class FirePage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='element.html',
                                object_list=[{'name': 'Flareon', 'number': 1},
                                             {'name': 'Charmander', 'number': 4}],
                                say_me='FIRE PAGE',
                                front_request=request).encode('UTF-8')


class WaterPage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='element.html',
                                object_list=[{'name': 'Megicarp', 'number': 11},
                                             {'name': 'Blastoise', 'number': 8}],
                                say_me='WATER PAGE',
                                front_request=request).encode('UTF-8')


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


class CreateCategory(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_name='create_category.html',
                                    say_me='Выберите название категории:',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=request, filename='post_data.txt')
            category = CategoryModel(request)
            category.insert_cat_list(category_list)
            return '200 OK', render(template_name='categores.html',
                                    object_list=category_list,
                                    say_me='Список доступных категорий:',
                                    front_request=request).encode('UTF-8')


class CategoryList(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='categores.html',
                                object_list=category_list,
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
            curs = CursFactory.create(request)
            if curs:
                curs.insert_curs_list(curs_list)
            return '200 OK', render(template_name='curses.html',
                                    object_list=curs_list,
                                    say_me='Список доступных курсов:',
                                    front_request=request).encode('UTF-8')


class CursList(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='curses.html',
                                object_list=curs_list,
                                say_me='Список доступных курсов:',
                                front_request=request).encode('UTF-8')