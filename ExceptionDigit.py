from datetime import datetime as dt
class ExceptionAge(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Ex():
    def validate(self, list_abit, page):
        if (all([list_abit.familiya.value,
                 list_abit.name.value,
                 list_abit.oth.value,
                 list_abit.age.value,
                 list_abit.phone.value,
                 list_abit.facultet.value,
                 any([list_abit.add_exam_abit1.value,
                      list_abit.add_exam_abit2.value,
                      list_abit.add_exam_abit3.value])])):
            list_abit.save_abit.disabled = False
            list_abit.change.disabled = False
        else:
            list_abit.save_abit.disabled = True
            list_abit.change.disabled = True
        page.update()


    def validate_facultet(self, list_facultet, page):
        if (all([list_facultet.name_fac.value,
                 list_facultet.opisanie.value])):
            list_facultet.save_fac.disabled = False
            list_facultet.change.disabled = False
        else:
            list_facultet.save_fac.disabled = True
            list_facultet.change.disabled = True
        page.update()

    def validate_exam(self, list_exam, page):
        if (all([list_exam.name_exam.value,
                 list_exam.date_exam.value,
                 list_exam.aud.value])):
            list_exam.save_exam.disabled = False
            list_exam.change.disabled = False
        else:
            list_exam.save_exam.disabled = True
            list_exam.change.disabled = True
        page.update()

    def povtor(self, flag, list_abit, page):
        try:
            if not flag:
                raise ExceptionAge("Такой уже есть")
        except ExceptionAge as e:
            list_abit.phone.error_text = e
        page.update()





    def try_ex_abit(self, list_abit, page):
        flag = True
        try:
            if not list_abit.age.value.isdigit():
                list_abit.age.value = ""
                raise ExceptionAge("В поле должно быть число")
            elif int(list_abit.age.value) < 16:
                list_abit.age.value = ""
                raise ExceptionAge("Должен быть больше 16")
            list_abit.age.error_text = None
        except ExceptionAge as e:
            flag = False
            list_abit.age.error_text = e

        try:
            if not list_abit.familiya.value.isalpha():
                list_abit.familiya.value = ""
                raise ExceptionAge("Содержит только буквы")
            elif list_abit.familiya.value[0].islower():
                list_abit.familiya.value = ""
                raise ExceptionAge("Начинается с заглавной  буквы")
            elif len(list_abit.familiya.value) < 2:
                list_abit.familiya.value = ""
                raise ExceptionAge("Должна быть длиннее")
            elif not list_abit.familiya.value[1:].islower():
                list_abit.familiya.value = ""
                raise ExceptionAge("Не имеет заглавных букв")
            list_abit.familiya.error_text = None
        except ExceptionAge as e:
            list_abit.familiya.error_text = e
            flag = False
        try:
            if not list_abit.name.value.isalpha():
                list_abit.name.value = ""
                raise ExceptionAge("Содержит только буквы")
            elif list_abit.name.value[0].islower():
                list_abit.name.value = ""
                raise ExceptionAge("Начинается с заглавной  буквы")
            elif len(list_abit.name.value) < 2:
                list_abit.name.value = ""
                raise ExceptionAge("Должно быть длиннее")
            elif not list_abit.name.value[1:].islower():
                list_abit.name.value = ""
                raise ExceptionAge("Не имеет заглавных букв")
            list_abit.name.error_text = None
        except ExceptionAge as e:
            list_abit.name.error_text = e
            flag = False
        try:
            if not list_abit.oth.value.isalpha():
                list_abit.oth.value = ""
                raise ExceptionAge("Содержит только буквы")
            elif list_abit.oth.value[0].islower():
                list_abit.oth.value = ""
                raise ExceptionAge("Начинается с заглавной  буквы")
            elif len(list_abit.oth.value) < 2:
                list_abit.oth.value = ""
                raise ExceptionAge("Должно быть длиннее")
            elif not list_abit.oth.value[1:].islower():
                list_abit.oth.value = ""
                raise ExceptionAge("Не имеет заглавных букв")
            list_abit.oth.error_text = None
        except ExceptionAge as e:
            list_abit.oth.error_text = e
            flag = False
        try:
            if not list_abit.phone.value.isdigit():
                list_abit.phone.value = ''
                raise ExceptionAge("Должен содержать только цифры")
            elif len(list_abit.phone.value) != 11:
                raise ExceptionAge("Неверный формат")
            list_abit.phone.error_text = None
        except ExceptionAge as e:
            flag = False
            list_abit.phone.error_text = e
        page.update()
        return flag


    def try_ex_exam(self, list_exam, page):
        date = list_exam.date_exam.value.split('.')
        flag = True
        try:
            dt.strptime(list_exam.date_exam.value, "%d.%m.%Y")
            list_exam.date_exam.error_text = None
        except ValueError:
            list_exam.date_exam.value = ""
            list_exam.date_exam.error_text = "Не существующая дата"
            flag = False
        try:
            if len(date) != 3:
                print(len(date))
                list_exam.date_exam.value = ""
                raise ExceptionAge("Не корректный ввод")
            list_exam.date_exam.error_text = None
        except ExceptionAge as e:
            list_exam.date_exam.error_text = e
            flag = False
        try:
            if not list_exam.aud.value.isdigit():
                list_exam.aud.value = ""
                raise ExceptionAge("Не содержит букв")
            elif len(list_exam.aud.value) != 4:
                list_exam.aud.value = ""
                raise ExceptionAge("Состоит из 4 цифр")
            list_exam.aud.error_text = None
        except ExceptionAge as e:
            list_exam.aud.error_text = e
            flag = False
        page.update()
        return flag

    def phone_valid(self, list_abit, page):
        try:
            list_abit.aud.value = ""
            raise ExceptionAge("Не содержит букв")
        except ExceptionAge as e:
            list_abit.aud.error_text = e
        page.update()




