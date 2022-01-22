def info_we_need(request):
    need_dict = {
        'method': request['method'],
        'fname': request['fname'],
        'lname': request['lname'],
        'email': request['email']
    }
    return need_dict
