import sqlite3
import  flet as ft


from ExceptionDigit import Ex


class DataBase:

    def __init__(self):
        self.class_ex = Ex()
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = """ CREATE TABLE IF NOT EXISTS СписокФакультетов(Название TEXT, Описание TEXT) """
            cursor.execute(query)
            query = """ CREATE TABLE IF NOT EXISTS Spisoks(Фамилия TEXT, Имя TEXT, Отчество TEXT, Возраст TEXT, Телефон TEXT, Факультет TEXT) """
            cursor.execute(query)
            query = """ CREATE TABLE IF NOT EXISTS СписокЭкзаменов(
            Название TEXT, Дата TEXT, Аудитория TEXT) """
            cursor.execute(query)
            query = """ CREATE TABLE IF NOT EXISTS СвязьЭкзаменовАбитуриентов(
                        Телефон TEXT, Экзамен TEXT, Оценка TEXT) """
            cursor.execute(query)



    def add_facultet(self, list_facultet, page):
        if not self.class_ex.validate_facultet(list_facultet, page):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" INSERT INTO СписокФакультетов(Название, Описание) VALUES('{list_facultet.name_fac.value}',
                 '{list_facultet.opisanie.value}') """
                cursor.execute(query)
                db.commit()
            list_facultet.name_fac.value = ''
            list_facultet.opisanie.value = ''
            quest = ft.AlertDialog(title=ft.Text("Факультет добавлен"))
            page.open(quest)
        page.update()



    def add_abiturient(self, list_abit, page):
        def add_exam_abit(phone, name, mark):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" INSERT INTO СвязьЭкзаменовАбитуриентов(Телефон, Экзамен, Оценка) VALUES('{phone}',
                                        '{name}', '{mark}') """
                cursor.execute(query)
                db.commit()

        def get_phone(name):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" SELECT * FROM Spisoks WHERE Телефон='{name}' """
                cursor.execute(query)
                db.commit()
                return cursor


        if not self.class_ex.validate(list_abit, page):
            if self.class_ex.try_ex_abit(list_abit, page):
                if len(list(get_phone(list_abit.phone.value))) == 0:
                    with sqlite3.connect('db/database.db') as db:
                        cursor = db.cursor()
                        query = f""" INSERT INTO Spisoks(Фамилия, Имя, Отчество, Возраст, Телефон, Факультет) VALUES(
                                                '{list_abit.familiya.value}', '{list_abit.name.value}', '{list_abit.oth.value}',
                                                 '{list_abit.age.value}', '{list_abit.phone.value}', '{list_abit.facultet.value}' ) """
                        cursor.execute(query)
                        db.commit()
                    if list_abit.add_exam_abit1.value:
                        add_exam_abit(list_abit.phone.value, list_abit.add_exam_abit1.value, list_abit.add_mark1.value)
                    if list_abit.add_exam_abit2.value:
                        add_exam_abit(list_abit.phone.value, list_abit.add_exam_abit2.value, list_abit.add_mark2.value)
                    if list_abit.add_exam_abit3.value:
                        add_exam_abit(list_abit.phone.value, list_abit.add_exam_abit3.value, list_abit.add_mark3.value)
                    list_abit.familiya.value = ''
                    list_abit.name.value = ''
                    list_abit.oth.value = ''
                    list_abit.age.value = ''
                    list_abit.facultet.value = ''
                    list_abit.add_exam_abit1.value = ''
                    list_abit.add_exam_abit2.value = ''
                    list_abit.add_exam_abit3.value = ''
                    list_abit.add_mark1.value = ''
                    list_abit.add_mark2.value = ''
                    list_abit.add_mark3.value = ''
                    list_abit.phone.value = ''
                    quest = ft.AlertDialog(title=ft.Text("Абитуриент добавлен"))
                    page.open(quest)
                else:
                    self.class_ex.povtor(False, list_abit, page)
        page.update()



    def add_exam(self, list_exam, page):
        def find_exam(date, aud):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" SELECT * FROM СписокЭкзаменов WHERE Дата='{date}' AND Аудитория='{aud}' """
                cursor.execute(query)
                db.commit()
            return cursor




        if not self.class_ex.validate_exam(list_exam, page):
            if self.class_ex.try_ex_exam(list_exam, page):
                if len(list(find_exam(list_exam.date_exam.value, list_exam.aud.value))) != 0:
                    dlg = ft.AlertDialog(
                        title=ft.Text("Выберите другой день или аудиторию. В этот день в данной аудитории уже проходит экзамен"))
                    page.open(dlg)
                else:
                    with sqlite3.connect('db/database.db') as db:
                        cursor = db.cursor()
                        query = f""" INSERT INTO СписокЭкзаменов(Название, Дата, Аудитория) VALUES(
                        '{list_exam.name_exam.value}', '{list_exam.date_exam.value}', '{list_exam.aud.value}') """
                        cursor.execute(query)
                        db.commit()
                    list_exam.name_exam.value = ''
                    list_exam.date_exam.value = ''
                    list_exam.aud.value = ''
                    quest = ft.AlertDialog(title=ft.Text("Экзамен добавлен"))
                    page.open(quest)
        page.update()



    def get_data_abit(self):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = """ SELECT * FROM Spisoks """
            cursor.execute(query)
            db.commit()
            return cursor

    def get_data_exam(self):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = """ SELECT * FROM СписокЭкзаменов """
            cursor.execute(query)
            db.commit()
            return cursor


    def get_data_facultet(self):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = """ SELECT * FROM СписокФакультетов """
            cursor.execute(query)
            db.commit()
            return cursor

    def del_abit(self, phone):
        def delete_svzy(phone):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" DELETE FROM СвязьЭкзаменовАбитуриентов WHERE Телефон='{phone}' """
                cursor.execute(query)
                db.commit()

        with sqlite3.connect('db/database.db') as db:
            delete_svzy(phone)
            cursor = db.cursor()
            query = f""" DELETE FROM Spisoks WHERE Телефон='{phone}' """
            cursor.execute(query)
            db.commit()


    def del_facultet(self, fac):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" DELETE FROM СписокФакультетов WHERE Название='{fac}' """
            cursor.execute(query)
            db.commit()


    def del_exam(self, name, date, aud):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" DELETE FROM СписокЭкзаменов WHERE Название='{name}' AND Дата='{date}' AND Аудитория='{aud}' """
            cursor.execute(query)
            db.commit()


    def change_abit(self,e, lv, page, list_abit, phone):
        def add_exam_abit(phone, name, mark):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" INSERT INTO СвязьЭкзаменовАбитуриентов(Телефон, Экзамен, Оценка) VALUES('{phone}',
                                        '{name}', '{mark}') """
                cursor.execute(query)
                db.commit()


        def delete_svzy(phone):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" DELETE FROM СвязьЭкзаменовАбитуриентов WHERE Телефон='{phone}' """
                cursor.execute(query)
                db.commit()


        if (self.class_ex.try_ex_abit(list_abit, page)):
            with sqlite3.connect('db/database.db') as db:
                cursor = db.cursor()
                query = f""" UPDATE Spisoks SET Фамилия='{list_abit.familiya.value}', Имя='{list_abit.name.value}',
                 Отчество='{list_abit.oth.value}', Возраст='{list_abit.age.value}', Телефон='{list_abit.phone.value}',
                  Факультет='{list_abit.facultet.value}' """
                cursor.execute(query)
                db.commit()
                delete_svzy(list_abit.phone.value)
                if list_abit.add_exam_abit1.value:
                    add_exam_abit(list_abit.phone.value, list_abit.add_exam_abit1.value, list_abit.add_mark1.value)
                if list_abit.add_exam_abit2.value:
                    add_exam_abit(list_abit.phone.value, list_abit.add_exam_abit2.value, list_abit.add_mark2.value)
                if list_abit.add_exam_abit3.value:
                    add_exam_abit(list_abit.phone.value, list_abit.add_exam_abit3.value, list_abit.add_mark3.value)

                page.remove(e)
                for i in range(len(list_abit.tabel_abiturient.rows)):
                    if list_abit.tabel_abiturient.rows[i].cells[4].content.value == phone:
                        list_abit.tabel_abiturient.rows[i].cells = [ft.DataCell(ft.Text(list_abit.familiya.value)),
                                                                    ft.DataCell(ft.Text(list_abit.name.value)),
                                                                    ft.DataCell(ft.Text(list_abit.oth.value)),
                                                                    ft.DataCell(ft.Text(list_abit.age.value)),
                                                                    ft.DataCell(ft.Text(list_abit.phone.value)),
                                                                    ft.DataCell(ft.Text(list_abit.facultet.value))]
                        break
                quest = ft.AlertDialog(title=ft.Text("Данные абитуриента изменены"))
                page.open(quest)
                page.add(lv)

        page.update()


    def change_facultet(self,e, lv, page, list_facultet, name_fac, i):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" UPDATE СписокФакультетов SET Название='{list_facultet.name_fac.value}', Описание='{list_facultet.opisanie.value}'
             WHERE Название='{name_fac}' """
            cursor.execute(query)
            query = f"""UPDATE Spisoks SET Факультет='{list_facultet.name_fac.value}' WHERE Факультет='{name_fac}' """
            cursor.execute(query)
            page.remove(e)
            list_facultet.tabel_facultet.rows[i].cells = [ft.DataCell(ft.Text(list_facultet.name_fac.value)),
                                                          ft.DataCell(ft.Text(list_facultet.opisanie.value))]
            quest = ft.AlertDialog(title=ft.Text("Данные факультета изменены"))
            page.open(quest)
            page.add(lv)
            db.commit()
        page.update()


    def change_exam(self, page, list_exam, name_exam, date, aud):
        if not self.class_ex.validate_exam(list_exam, page):
            if self.class_ex.try_ex_exam(list_exam, page):
                with sqlite3.connect('db/database.db') as db:
                    cursor = db.cursor()
                    query = f""" UPDATE СписокЭкзаменов SET Название='{list_exam.name_exam.value}', Дата='{list_exam.date_exam.value}',
                     Аудитория='{list_exam.aud.value}' WHERE Название='{name_exam}' AND Дата='{date}' AND
                     Аудитория='{aud}' """
                    cursor.execute(query)
                    quest = ft.AlertDialog(title=ft.Text("Данные экзамена изменены"))
                    page.open(quest)
                    db.commit()


    def get_on_facultet(self, fac):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM Spisoks WHERE Факультет='{fac}' """
            cursor.execute(query)
            db.commit()
            return cursor

    def get_on_exam(self, name):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM СвязьЭкзаменовАбитуриентов WHERE Экзамен='{name}' """
            cursor.execute(query)
            db.commit()
            return cursor

    def get_abit_for_phone(self, name):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM Spisoks WHERE Телефон='{name}' """
            cursor.execute(query)
            db.commit()
            return cursor

    def get_abit_for_phone_exam(self, phone, name):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM СвязьЭкзаменовАбитуриентов WHERE Телефон='{phone}' AND Экзамен='{name}' """
            cursor.execute(query)
            db.commit()
            return cursor

    def find_svzy(self, phone):
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM СвязьЭкзаменовАбитуриентов WHERE Телефон='{phone}' """
            cursor.execute(query)
            db.commit()
        return cursor


    def find(self, str):
        str = str.capitalize()
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM Spisoks WHERE Фамилия='{str}' OR Имя='{str}' OR
                             Отчество='{str}' OR Возраст='{str}' OR Телефон='{str}' OR
                              Факультет='{str}' """
            cursor.execute(query)
            db.commit()
        return cursor

    def find_exam(self, str):
        str = str.upper()
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM СписокЭкзаменов WHERE Название='{str}' OR Дата='{str}' OR
             Аудитория='{str}' """
            cursor.execute(query)
            db.commit()

        return cursor


    def find_facultet(self, str):
        str = str.upper()
        with sqlite3.connect('db/database.db') as db:
            cursor = db.cursor()
            query = f""" SELECT * FROM СписокФакультетов WHERE Название='{str}' OR Описание='{str}' """
            cursor.execute(query)
            db.commit()

        return cursor















