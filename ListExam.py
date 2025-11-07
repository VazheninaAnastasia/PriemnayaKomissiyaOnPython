from DataBase import DataBase
import flet as ft

from ListAbit import ListAbit


class ListExam():
    def __init__(self):
        self.tabel_exam = ft.DataTable(width=650, border=ft.border.all(2, "blue"), rows=None,
                                  vertical_lines=ft.BorderSide(3, "#A0CAFD"),
                                  columns=[ft.DataColumn(ft.Text("Название")),
                                           ft.DataColumn(ft.Text("Дата")),
                                           ft.DataColumn(ft.Text("Аудитория"))])
       # self.update_or_delete = ft.AlertDialog(title=ft.Text("Выберите"),
        #                                       actions=[ft.TextButton("Удалить"),
         #                                               ft.TextButton("Изменить"),
          #                                              ft.TextButton("Список")])
        self.db = DataBase()
        self.name_exam_for_card = ft.Text("Название",
                                                    color='#A0CAFD', text_align=ft.TextAlign.LEFT, width=200,
                                                    size=18)
        self.date_exam_for_card = ft.Text("Дата",
                                                    color='#A0CAFD', text_align=ft.TextAlign.LEFT, width=200,
                                                    size=18)
        self.aud_for_card = ft.Text("Аудитория",
                                                    color='#A0CAFD', text_align=ft.TextAlign.LEFT, width=200,
                                                    size=18)
        self.btn_exam = ft.ElevatedButton(content=ft.Text('Список экзаменов', size=16), width=200, height=50)
        self.dr = ft.dropdown.Option("Экзамен")
        self.name_exam = ft.TextField(label='Название', width=200)
        self.date_exam = ft.TextField(label='Дата', width=200, hint_text="дд.мм.гггг")
        self.aud = ft.TextField(label='Аудитория', width=200)
        self.save_exam = ft.ElevatedButton(content=ft.Text('Сохранить', size=16), width=200, height=50,
                                           disabled=True)
        self.change = ft.ElevatedButton(content=ft.Text('Изменить', size=16), width=200, height=50,
                                           disabled=True)

        self.card = ft.Container(ft.Column([ft.Text("Карточка экзамена",
                                                    color='#A0CAFD', text_align=ft.TextAlign.CENTER, width=200,
                                                    size=20),
                                            self.name_exam, self.date_exam, self.aud, self.save_exam]))

        self.card_exam = ft.Container(ft.Column([ft.Text("Карточка экзамена",
                                                         color='#A0CAFD', text_align=ft.TextAlign.CENTER, width=200,
                                                         size=20), self.name_exam_for_card, self.date_exam_for_card, self.aud_for_card]))
        self.delit_btn = ft.ElevatedButton(content=ft.Text('Удалить', size=16), width=200, height=50)
        self.change_btn = ft.ElevatedButton(content=ft.Text('Изменить', size=16), width=200, height=50)
        self.list = ft.ElevatedButton(content=ft.Text('Список абитуриентов, сдающих экзамен', size=16), width=350, height=50)
        self.actions = ft.Row([self.delit_btn, self.change_btn, self.list])
        self.quest = ft.AlertDialog(title=ft.Text("Вы уверены, что хотите удалить этот экзамен?"),
                                               actions=[ft.TextButton("Да"),
                                                        ft.TextButton("Нет")])
        self.card_for_change = ft.Container(ft.Column([ft.Text("Карточка экзамена",
                                                    color='#A0CAFD', text_align=ft.TextAlign.CENTER, width=200,
                                                    size=20),
                                            self.name_exam, self.date_exam, self.aud, self.change]))



        self.list_abit = ListAbit()


