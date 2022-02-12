import json


class CategoryDirector:
    category_dict = {}

    @classmethod
    def update(cls, category_model):
        if category_model.category_name not in cls.category_dict:
            cls.category_dict[category_model.category_name] = category_model

    @classmethod
    def insert_curs_to_category(cls, curs):
        if curs.curs_cat in cls.category_dict:
            cls.category_dict[curs.curs_cat].insert_curs(curs)

    @classmethod
    def memento_category_json(cls, cat_name):
        data = []
        if cat_name == 'all':
            for c_name in cls.category_dict:
                curs_list = cls.category_dict[c_name].curses
                data.append({c_name: [curs.curs_name for curs in curs_list]})
        else:
            curs_list = cls.category_dict[cat_name].curses
            data = {cat_name: [curs.curs_name for curs in curs_list]}

        with open('templates/memento_category.json', 'w') as outfile:
            json.dump(data, outfile)

    @classmethod
    def return_curs_by_name(cls, category_name, curs_name_):
        curs_list = cls.category_dict[category_name].curses
        for curs in curs_list:
            if curs.curs_name == curs_name_:
                return curs


class CursDirector:

    @staticmethod
    def insert_student_to_curs(curs, student):
        if student.id not in [stud.id for stud in curs.students_list]:
            curs.students_list.append(student)

    @staticmethod
    def insert_student_to_students_list(student):
        student.go_to_list()
