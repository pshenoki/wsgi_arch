from time import time


def info_we_need(request):
    need_dict = {
        'method': request['method'],
        'fname': request['fname'],
        'lname': request['lname'],
        'email': request['email']
    }
    return need_dict


def debug(acls):
    def inner(*args, **kwargs):
        start = time()
        result = acls(*args, **kwargs)
        end = time()
        print('DEBUG->', result.__class__.__name__, end - start)
        return result

    return inner
