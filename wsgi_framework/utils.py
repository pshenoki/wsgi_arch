def check_slash(route: str) -> str:
    """ Если есть '/' убирает его """
    if route == '/':
        return route
    return route[:-1] if route[-1] == '/' else route


def parse_input_data(data: str) -> dict:
    """ Преобразуем post-строку в словарь """
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result


def get_wsgi_input_data(env) -> bytes:
    """ Принимаем байтстроку  """
    # получаем длину тела
    content_length_data = env.get('CONTENT_LENGTH')
    # приводим к int
    content_length = int(content_length_data) if content_length_data else 0
    # считываем данные если они есть
    data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
    return data


def parse_wsgi_input_data(data: bytes) -> dict:
    """ Декодируем байты в строку """
    result = {}
    if data:
        # декодируем данные
        data_str = data.decode(encoding='utf-8')
        # собираем их в словарь
        result = parse_input_data(data_str)
    return result


def save_to_file(data, filename):
    with open(filename, 'a', encoding='UTF-8') as outfile:
        outfile.write(f"{data}\n")
