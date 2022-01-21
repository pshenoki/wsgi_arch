from wsgi_framework.page_controllers import PageController
from wsgi_framework.shablonizator import render
from config import TEMPLATE_PATH


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
        return '200 OK', render(template_path=TEMPLATE_PATH,
                                template_name='contact.html',
                                say_me='CONTACTS PAGE',
                                front_request=request).encode('UTF-8')
