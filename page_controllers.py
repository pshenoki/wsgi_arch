from wsgi_framework.page_controllers import PageController
from wsgi_framework.shablonizator import render
from config import TEMPLATE_PATH
from wsgi_framework.utils import save_to_file
from utils import info_we_need


class IndexPage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_path=TEMPLATE_PATH,
                                template_name='index.html',
                                say_me='MY HOME PAGE',
                                front_request=request).encode('UTF-8')


class FirePage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_path=TEMPLATE_PATH,
                                template_name='element.html',
                                object_list=[{'name': 'Flareon', 'number': 1},
                                             {'name': 'Charmander', 'number': 4}],
                                say_me='FIRE PAGE',
                                front_request=request).encode('UTF-8')


class WaterPage(PageController):
    def __call__(self, request):
        return '200 OK', render(template_path=TEMPLATE_PATH,
                                template_name='element.html',
                                object_list=[{'name': 'Megicarp', 'number': 11},
                                             {'name': 'Blastoise', 'number': 8}],
                                say_me='WATER PAGE',
                                front_request=request).encode('UTF-8')


class ContactPage(PageController):
    def __call__(self, request):

        if request['method'] == "GET":
            save_to_file(data=request, filename='get_data.txt')
            return '200 OK', render(template_path=TEMPLATE_PATH,
                                    template_name='contact.html',
                                    say_me='CONTACTS PAGE',
                                    front_request=request).encode('UTF-8')

        elif request['method'] == "POST":
            save_to_file(data=info_we_need(request), filename='post_data.txt')
            return '200 OK', render(template_path=TEMPLATE_PATH,
                                    template_name='greeting.html',
                                    say_me='Поздравляю',
                                    front_request=request).encode('UTF-8')
