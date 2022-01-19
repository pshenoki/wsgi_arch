def check_slash(route):
    if route == '/':
        return route
    return route[:-1] if route[-1] == '/' else route