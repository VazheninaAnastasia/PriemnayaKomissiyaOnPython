import flet as ft
from DataBase import DataBase


class ListFacultet():
    def __init__(self):
        self.tabel_facultet = ft.DataTable(width=650,
                                      border=ft.border.all(2, "blue"),
                                      rows=None,
                                      vertical_lines=ft.BorderSide(3, "blue"),
                                      columns=[ft.DataColumn(ft.Text('Название')),
                                               ft.DataColumn(ft.Text("Описание"))])
        self.update_or_delete = ft.AlertDialog(title=ft.Text("Выберите"),
                                               actions=[ft.TextButton("Удалить"),
                                                        ft.TextButton("Изменить"), ft.TextButton("Список")])
        self.db = DataBase()
        self.btn_fac = ft.ElevatedButton(content=ft.Text('Список факультетов', size=16), width=200, height=50)
        self.dr = ft.dropdown.Option("Факультет")
        self.name_fac = ft.TextField(label='Название',
                                width=200)
        self.opisanie = ft.TextField(label='Расшифровка',
                                width=600,
                                multiline=True)
        self.save_fac = ft.ElevatedButton(content=ft.Text('Сохранить', size=16), width=200, height=50,
                                          disabled=True)
        self.change = ft.ElevatedButton(content=ft.Text('Изменить', size=16), width=200, height=50,
                                          disabled=True)
        self.card = ft.Container(ft.Column([ft.Text("Карточка факультета", color='#A0CAFD',
                           text_align=ft.TextAlign.CENTER, width=200, size=20),
                                self.name_fac, self.opisanie, self.save_fac]))

        self.card_for_change = ft.Container(ft.Column([ft.Text("Карточка факультета", color='#A0CAFD',
                           text_align=ft.TextAlign.CENTER, width=200, size=20),
                                self.name_fac, self.opisanie, self.change]))
        self.quest = ft.AlertDialog(title=ft.Text("Вы уверены, что хотите удалить этот факультет?"),
                                    actions=[ft.TextButton("Да"),
                                             ft.TextButton("Нет")])










