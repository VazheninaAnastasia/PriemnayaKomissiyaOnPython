import flet as ft

from DataBase import DataBase


class ListAbit():
    def __init__(self):
        self.tabel_abiturient = ft.DataTable(
                                        border=ft.border.all(2, "blue"),
                                        rows=None,
                                        vertical_lines=ft.BorderSide(3, "#A0CAFD"),
                                        columns=[ft.DataColumn(ft.Text("Фамилия")),
                                                 ft.DataColumn(ft.Text("Имя")),
                                                 ft.DataColumn(ft.Text("Отчество")),
                                                 ft.DataColumn(ft.Text("Возраст")),
                                                 ft.DataColumn(ft.Text("Телефон")),
                                                 ft.DataColumn(ft.Text("Факультет"))],)
        self.tabel_abiturient_with_exam = ft.DataTable(
            border=ft.border.all(2, "blue"),
            rows=None,
            vertical_lines=ft.BorderSide(3, "#A0CAFD"),
            columns=[ft.DataColumn(ft.Text("Фамилия")),
                     ft.DataColumn(ft.Text("Имя")),
                     ft.DataColumn(ft.Text("Отчество")),
                     ft.DataColumn(ft.Text("Факультет")),
                     ft.DataColumn(ft.Text("Экзамен")),
                     ft.DataColumn(ft.Text("Оценка"))], )
        self.update_or_delete = ft.AlertDialog(title=ft.Text("Выберите"),
                                               actions=[ft.TextButton("Удалить"),
                                                        ft.TextButton("Изменить")])
        self.db = DataBase()
        self.familiya = ft.TextField(label='Фамилия', width=200)
        self.name = ft.TextField(label='Имя', width=200)
        self.oth = ft.TextField(label='Отчество',width=200,)
        self.age = ft.TextField(label='Возраст', width=200,)
        self.phone = ft.TextField(label='Номер телефона', width=200, hint_text='8xxxxxxxxxx')
        self.facultet = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                    size=16,
                                                    color='#A0CAFD',
                                                    text_align=ft.TextAlign.CENTER),
                               prefix_text='Факультет: ',
                               height=50,
                               width=300,
                               border_radius=27,
                               text_size=16,
                               options=[ft.dropdown.Option(i[0]) for i in self.db.get_data_facultet()])
        self.add_exam_abit1 = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                               size=16,
                                                               color='#A0CAFD',
                                                               text_align=ft.TextAlign.CENTER),
                                          prefix_text="Экзамен:",
                                          height=50,
                                          width=350,
                                          border_radius=27,
                                          text_size=16,
                                          options=[ft.dropdown.Option(f"{i[0]}, {i[1]}") for i in self.db.get_data_exam()])
        self.add_mark1 = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                          size=16,
                                                          color='#A0CAFD',
                                                          text_align=ft.TextAlign.CENTER),
                                     prefix_text="Оценка:",
                                     height=50,
                                     width=200,
                                     border_radius=27,
                                     text_size=16,
                                     options=[ft.dropdown.Option(i) for i in range(2, 6)])
        self.add_exam_abit2 = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                              size=16,
                                                              color='#A0CAFD',
                                                              text_align=ft.TextAlign.CENTER),
                                         prefix_text="Экзамен:",
                                         height=50,
                                         width=350,
                                         border_radius=27,
                                         text_size=16,
                                         options=[ft.dropdown.Option(f"{i[0]}, {i[1]}") for i in
                                                  self.db.get_data_exam()])
        self.add_mark2 = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                         size=16,
                                                         color='#A0CAFD',
                                                         text_align=ft.TextAlign.CENTER),
                                    prefix_text="Оценка:",
                                    height=50,
                                    width=200,
                                    border_radius=27,
                                    text_size=16,
                                    options=[ft.dropdown.Option(i) for i in range(2, 6)])
        self.add_exam_abit3 = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                              size=16,
                                                              color='#A0CAFD',
                                                              text_align=ft.TextAlign.CENTER),
                                         prefix_text="Экзамен:",
                                         height=50,
                                         width=350,
                                         border_radius=27,
                                         text_size=16,
                                         options=[ft.dropdown.Option(f"{i[0]}, {i[1]}") for i in
                                                  self.db.get_data_exam()])
        self.add_mark3 = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                         size=16,
                                                         color='#A0CAFD',
                                                         text_align=ft.TextAlign.CENTER),
                                    prefix_text="Оценка:",
                                    height=50,
                                    width=200,
                                    border_radius=27,
                                    text_size=16,
                                    options=[ft.dropdown.Option(i) for i in range(2, 6)])
        self.save_abit = ft.ElevatedButton(content=ft.Text('Сохранить', size=16), width=200, height=50,
                                           disabled=True)
        self.change = ft.ElevatedButton(content=ft.Text('Изменить', size=16), width=200, height=50,
                                           disabled=True)
        self.btn_abit = ft.ElevatedButton(content=ft.Text('Список абитуриентов', size=16), width=200, height=50)
        self.card = ft.Container(ft.Column([ft.Text("Анкета абитуриента",
                                                    color='#A0CAFD', text_align=ft.TextAlign.CENTER,width=200, size=20),
                                            ft.Row([ft.Column([self.familiya, self.name, self.oth, self.age, self.save_abit]),
                                                    ft.Column([self.phone, self.facultet,
                                                               ft.Row([self.add_exam_abit1, self.add_mark1]),
                                                               ft.Row([self.add_exam_abit2, self.add_mark2]),
                                                               ft.Row([self.add_exam_abit3, self.add_mark3])
                                                               ])])]))
        self.card_for_change = ft.Container(ft.Column([ft.Text("Анкета абитуриента",
                                                    color='#A0CAFD', text_align=ft.TextAlign.CENTER, width=200,
                                                    size=20),
                                            ft.Row([ft.Column(
                                                [self.familiya, self.name, self.oth, self.age, self.change]),
                                                    ft.Column([self.phone, self.facultet,
                                                               ft.Row([self.add_exam_abit1, self.add_mark1]),
                                                               ft.Row([self.add_exam_abit2, self.add_mark2]),
                                                               ft.Row([self.add_exam_abit3, self.add_mark3])])])]))
        self.quest = ft.AlertDialog(title=ft.Text("Вы уверены, что хотите удалить этого абитуриента?"),
                                    actions=[ft.TextButton("Да"),
                                             ft.TextButton("Нет")])
        self.dr = ft.dropdown.Option("Абитуриента")















