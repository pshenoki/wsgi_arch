from abc import ABC, abstractmethod


class Mapper(ABC):
    def __init__(self, connect):
        self.connection = connect
        self.cursor = connect.cursor()

    @abstractmethod
    def select_all(self):
        pass


class TableCreator:
    def __init__(self, connect):
        self.connection = connect
        self.cursor = connect.cursor()

    def create_tables(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS student (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
            lastname VARCHAR (32), 
            firstname VARCHAR (32),
            email  VARCHAR (64)
            );
            """)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS category (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
            category_name VARCHAR (32) UNIQUE
            );
            """)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS curs (
            curs_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
            curs_name VARCHAR (32),
            category_name VARCHAR (32),
            curs_type VARCHAR (32)
            );
            """)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS curs_student_rel (
            curs_id INTEGER,
            student_id INTEGER);
            """)

            self.cursor.execute("""CREATE TABLE IF NOT EXISTS student_tokens (
             student_id INTEGER,
             tokens INTEGER);
             """)

            print('таблицы созданы')


class StudentMapper(Mapper):

    def select_all(self):
        result = self.cursor.execute(""" select * from student """)
        return result.fetchall()

    def select_student_info(self):
        result = self.cursor.execute(""" select * from student st join curs_student_rel rel 
                    on st.student_id = rel.student_id""")
        return result.fetchall()

    def select_all_in_curs(self, curs_id):
        self.cursor.execute(f""" select st.* from student st join curs_student_rel rel
          on st.student_id = rel.student_id where rel.curs_id = {curs_id}""")

    def create_student(self, lname, fname, email):
        self.cursor.execute(f"""INSERT INTO student (lastname, firstname, email)
                            VALUES ('{lname}', '{fname}', '{email}')""")
        self.connection.commit()

    def return_id_by_name(self, lname, fname):
        id_stud = self.cursor.execute(f"""select student_id from student 
                                      where (lastname, firstname) =  ('{lname}', '{fname}') 
                                      order by student_id desc limit 1 """)
        return id_stud.fetchone()[0]

    def insert_student_to_curs(self, curs_id, stud_id):
        self.cursor.execute(f"""INSERT INTO curs_student_rel (curs_id, student_id)
                            VALUES ('{stud_id}', '{curs_id}')""")

        self.connection.commit()

    def insert_tokens_to_student(self, stud_id, tokens):
        self.cursor.execute(f"""INSERT INTO curs_student_rel (curs_id, student_id)
                            VALUES ('{stud_id}', '{tokens}')""")

        self.connection.commit()


class CursMapper(Mapper):

    def select_all(self):
        result = self.cursor.execute(""" select * from curs """)
        return result.fetchall()

    def select_all_curs_in_category(self, cat_name):
        self.cursor.execute(f""" select * from curs where cat_name = '{cat_name}'""")

    def select_curs_id_by_data(self, cat_name, curs_name):
        self.cursor.execute(f""" select curs_id from curs where 
                                 (category_name, curs_name) = ('{cat_name}', '{curs_name}')""")

    def create_curs(self, curs_name, cat_name, curs_type):
        self.cursor.execute(f"""INSERT INTO curs (curs_name, category_name, curs_type)
                            VALUES ('{curs_name}', '{cat_name}', '{curs_type}')
                             ON CONFLICT DO NOTHING """)
        self.connection.commit()


class CategoryMapper(Mapper):

    def select_all(self):
        with self.connection:
            result = self.cursor.execute(""" select category_name from category """)
            cat_list = [cat[0] for cat in result.fetchall()]
            return cat_list

    def create_category(self, cat_name):
        with self.connection:
            self.cursor.execute(f""" INSERT INTO category (category_name)
                                VALUES ('{cat_name}') """)
            self.connection.commit()

    def select_category_by_id(self, cat_id):
        with self.connection:
            result = self.cursor.execute(f""" select category_name  from category
                                        where category_id = '{cat_id}' """)
            return result.fetchone()[0]
