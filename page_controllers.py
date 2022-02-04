from wsgi_framework.page_controllers import PageController
from wsgi_framework.shablonizator import render
from wsgi_framework.utils import save_to_file
from utils import info_we_need
from models import Director
from utils import debug


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
            Director.update_category_dict(cat)
            return '200 OK', render(template_name='categores.html',
                                    object_list=Director.category_dict,
                                    say_me='Список доступных категорий и курсов:',
                                    front_request=request).encode('UTF-8')


class CategoryList(PageController):
    def __call__(self, request):
        return '200 OK', render(template_name='categores.html',
                                object_list=Director.category_dict,
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
            Director.insert_curs_to_category(curs)
            return '200 OK', render(template_name='categores.html',
                                    object_list=Director.category_dict,
                                    say_me='Список доступных категорий и курсов:',
                                    front_request=request).encode('UTF-8')
