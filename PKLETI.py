import  flet as ft
from DataBase import DataBase
from ListAbit import ListAbit
from ListExam import ListExam
from ListFacultet import ListFacultet
from ExceptionDigit import Ex
from Othet import Othet


class Window():
    def __init__(self):
        self.page = None
        self.db = DataBase()
        self.lv = ft.ListView(expand=1,
                              spacing=10,
                              padding=20,
                              auto_scroll=True,
                              controls=None)
        self.card = ft.Card(width=820,
                            height=450,
                            color='#111418',
                            content=None,
                            margin=20)
        self.othet_class = Othet()
        self.list_abit = ListAbit()
        self.list_facultet = ListFacultet()
        self.list_exam = ListExam()
        self.class_ex = Ex()
        self.othet = ft.Dropdown(hint_content=ft.Text('выбрать',
                                                    size=16,
                                                    color='#A0CAFD',
                                                    text_align=ft.TextAlign.CENTER),
                               prefix_text='Отчет: ',
                               height=50,
                               width=300,
                               border_radius=27,
                               text_size=16,
                               options=[ft.dropdown.Option("По экзаменам",on_click=lambda e:self.othet_class.othet_exam()),
                                        ft.dropdown.Option("По абитуриентам", on_click=lambda e:self.othet_class.othet_abiturient())])
        self.find_button = ft.IconButton(icon=ft.Icons.SEARCH_SHARP, icon_size=25, tooltip="Найти", height=40, disabled=True)
        self.serch_str = ft.SearchBar(view_elevation=4, divider_color='white', bar_hint_text="Поиск")

        self.find_str = ft.Row([self.serch_str, self.find_button])

    def main(self, page: ft.Page):
        def proverka(vidget):
            if (self.card in self.page and vidget):
                self.page.remove(self.card)
                self.page.add(self.lv)
            elif (self.lv in self.page and not vidget):
                self.page.remove(self.lv)
                self.find_button.disabled = True
                self.page.add(self.card)


        def open_alert_dialog(e, phone):
            self.page.open(self.list_abit.update_or_delete)
            self.list_abit.update_or_delete.actions[0].on_click = lambda e: self.page.open(self.list_abit.quest)
            self.list_abit.update_or_delete.actions[1].on_click = lambda e: update_abit(e, phone)
            self.list_abit.quest.actions[0].on_click = lambda e: delit_abit(e, phone)
            self.page.update()


        def open_alert_dialog_facultet(e, fac):
            self.page.open(self.list_facultet.update_or_delete)
            self.list_facultet.update_or_delete.actions[0].on_click = lambda e: self.page.open(self.list_facultet.quest)
            self.list_facultet.update_or_delete.actions[1].on_click = lambda e: update_facultet(e, fac)
            self.list_facultet.update_or_delete.actions[2].on_click = lambda e: open_on_facultet(e, fac)
            self.list_facultet.quest.actions[0].on_click = lambda e: delit_facultet(e, fac)
            self.page.update()


        def open(e):
            self.find_button.disabled = False
            match e.control:
                case self.list_abit.btn_abit:
                    self.list_abit.tabel_abiturient.rows = []
                    for i in self.db.get_data_abit():
                        self.list_abit.tabel_abiturient.rows.append(ft.DataRow(
                            cells=[ft.DataCell(ft.Text(j)) for j in i],
                            on_select_changed=lambda e: open_alert_dialog(e, e.control.cells[4].content.value)))
                    self.lv.controls = [self.list_abit.tabel_abiturient]
                case self.list_exam.btn_exam:
                    self.list_exam.tabel_exam.rows = []
                    for i in self.db.get_data_exam():
                        self.list_exam.tabel_exam.rows.append(ft.DataRow(
                            cells=[ft.DataCell(ft.Text(j)) for j in i], on_select_changed=lambda e: open_card_exam(e)))
                    self.lv.controls = [self.list_exam.tabel_exam]
                case self.list_facultet.btn_fac:
                    self.list_facultet.tabel_facultet.rows = []
                    for i in self.db.get_data_facultet():
                        self.list_facultet.tabel_facultet.rows.append(ft.DataRow(
                            cells=[ft.DataCell(ft.Text(j)) for j in i],
                            on_select_changed=lambda e: open_alert_dialog_facultet(e, e.control.cells[0].content.value)))
                    self.lv.controls = [self.list_facultet.tabel_facultet]
                case self.list_exam.change:
                    self.list_exam.tabel_exam.rows = []
                    for i in self.db.get_data_exam():
                        self.list_exam.tabel_exam.rows.append(ft.DataRow(
                            cells=[ft.DataCell(ft.Text(j)) for j in i], on_select_changed=lambda e: open_card_exam(e)))
                    self.lv.controls = [self.list_exam.tabel_exam]

            proverka(True)
            self.page.update()


        def open_on_exam(e, exam, date):
            self.list_abit.tabel_abiturient_with_exam.rows = []
            for i in self.db.get_on_exam(exam + ", " + date):
                for j in self.db.get_abit_for_phone(i[0]):
                    list_for_add = [j[k] for k in range(3)]
                    list_for_add.append(j[5])
                    for k in self.db.get_abit_for_phone_exam(j[4], exam + ", " + date):
                        list_for_add.append(k[1])
                        list_for_add.append(k[2])
                    self.list_abit.tabel_abiturient_with_exam.rows.append(ft.DataRow(
                        cells=[ft.DataCell(ft.Text(p)) for p in list_for_add],))
            self.page.remove(self.card)
            self.lv.controls = [self.list_abit.tabel_abiturient_with_exam]
            self.page.add(self.lv)
            self.page.update()


        def open_card_exam(e):
            self.page.remove(self.lv)
            name_exam = e.control.cells[0].content.value
            date = e.control.cells[1].content.value
            aud = e.control.cells[2].content.value
            self.list_exam.card_exam.content = ft.Container(ft.Column([ft.Text("Карточка экзамена",
                                                         color='#A0CAFD', text_align=ft.TextAlign.CENTER, width=200,
                                                         size=20),
                                                                       self.list_exam.name_exam_for_card,
                                                                       ft.Text(e.control.cells[0].content.value),
                                                                       self.list_exam.date_exam_for_card,
                                                                       ft.Text(e.control.cells[1].content.value),
                                                                       self.list_exam.aud_for_card,
                                                                       ft.Text(e.control.cells[2].content.value), self.list_exam.actions]))
            self.card.content = self.list_exam.card_exam

            self.list_exam.quest.actions[0].on_click = lambda e: delit_exam(e, name_exam, date, aud)
            self.list_exam.change_btn.on_click = lambda e: update_exam(e, name_exam, date, aud)
            self.list_exam.list.on_click = lambda e: open_on_exam(e, name_exam, date)
            self.page.add(self.card)
            self.page.update()


        def open_card(e):
            match e.control:
                case self.list_abit.dr:
                    self.card.content = self.list_abit.card
                    self.list_abit.familiya.error_text = None
                    self.list_abit.name.error_text = None
                    self.list_abit.oth.error_text = None
                    self.list_abit.age.error_text = None
                    self.list_abit.phone.error_text = None
                    self.list_abit.facultet.error_text = None
                    self.list_abit.add_exam_abit1.error_text = None
                    self.list_abit.add_mark1.error_text = None
                    self.list_abit.familiya.value = ''
                    self.list_abit.name.value = ''
                    self.list_abit.oth.value = ''
                    self.list_abit.age.value = ''
                    self.list_abit.facultet.value = ''
                    self.list_abit.add_exam_abit1.value = ''
                    self.list_abit.add_mark1.value = ''
                    self.list_abit.phone.value = ''
                    self.list_abit.facultet.options = [ft.dropdown.Option(i[0]) for i in self.db.get_data_facultet()]
                    self.list_abit.add_exam_abit1.options = [ft.dropdown.Option(f"{i[0]}, {i[1]}") for i in self.db.get_data_exam()]
                    self.page.update()
                case self.list_exam.dr:
                    self.card.content = self.list_exam.card
                    self.list_exam.name_exam.error_text = None
                    self.list_exam.date_exam.error_text = None
                    self.list_exam.aud.error_text = None
                    self.list_exam.name_exam.value = ''
                    self.list_exam.date_exam.value = ''
                    self.list_exam.aud.value = ''
                    self.page.update()
                case self.list_facultet.dr:
                    self.card.content = self.list_facultet.card
                    self.list_facultet.name_fac.error_text = None
                    self.list_facultet.opisanie.error_text = None
                    self.list_facultet.opisanie.value = ''
                    self.list_facultet.name_fac.value = ''
                    self.page.update()
            proverka(False)
            self.page.update()



        def delit_abit(e, phone):
            self.page.close(self.list_abit.quest)
            self.db.del_abit(phone)
            for i in range(len(self.list_abit.tabel_abiturient.rows)):
                if self.list_abit.tabel_abiturient.rows[i].cells[4].content.value == phone:
                    self.list_abit.tabel_abiturient.rows.pop(i)
                    break
            self.page.update()


        def delit_facultet(e, fac):
            self.page.close(self.list_facultet.quest)
            self.db.del_facultet(fac)
            for i in range(len(self.list_facultet.tabel_facultet.rows)):
                if self.list_facultet.tabel_facultet.rows[i].cells[0].content.value == fac:
                    self.list_facultet.tabel_facultet.rows.pop(i)
                    self.list_abit.facultet.options=[ft.dropdown.Option(i[0]) for i in self.db.get_data_facultet()]
                    break
            self.page.update()


        def delit_exam(e, name_exam, date, aud):
            self.page.close(self.list_exam.quest)
            self.page.remove(self.card)
            self.page.add(self.lv)
            self.db.del_exam(name_exam, date, aud)
            for i in range(len(self.list_exam.tabel_exam.rows)):
                if (self.list_exam.tabel_exam.rows[i].cells[0].content.value == name_exam and
                        self.list_exam.tabel_exam.rows[i].cells[1].content.value == date and
                        self.list_exam.tabel_exam.rows[i].cells[2].content.value == aud):
                    self.list_exam.tabel_exam.rows.pop(i)
                    self.list_abit.add_exam_abit1.options = [ft.dropdown.Option(f"{i[0]}, {i[1]}") for i in self.db.get_data_exam()]

                    break
            self.page.update()


        def update_abit(e, phone):
            self.page.close(self.list_abit.update_or_delete)
            for i in range(len(self.list_abit.tabel_abiturient.rows)):
                if self.list_abit.tabel_abiturient.rows[i].cells[4].content.value == phone:
                    self.page.remove(self.lv)
                    self.list_abit.familiya.value = self.list_abit.tabel_abiturient.rows[i].cells[0].content.value
                    self.list_abit.name.value = self.list_abit.tabel_abiturient.rows[i].cells[1].content.value
                    self.list_abit.oth.value = self.list_abit.tabel_abiturient.rows[i].cells[2].content.value
                    self.list_abit.age.value = self.list_abit.tabel_abiturient.rows[i].cells[3].content.value
                    self.list_abit.phone.value = self.list_abit.tabel_abiturient.rows[i].cells[4].content.value
                    self.list_abit.facultet.value = self.list_abit.tabel_abiturient.rows[i].cells[5].content.value
                    get_exam = list(self.db.find_svzy(phone))
                    count = len(get_exam)
                    if count >= 1:
                        self.list_abit.add_exam_abit1.value = get_exam[0][1]
                        self.list_abit.add_mark1.value = get_exam[0][2]
                    if count >= 2:
                        self.list_abit.add_exam_abit2.value = get_exam[1][1]
                        self.list_abit.add_mark2.value = get_exam[1][2]
                    if count == 3:
                        self.list_abit.add_exam_abit3.value = get_exam[2][1]
                        self.list_abit.add_mark3.value = get_exam[2][2]

                    self.card.content = self.list_abit.card
                    self.list_abit.familiya.error_text = None
                    self.list_abit.name.error_text = None
                    self.list_abit.oth.error_text = None
                    self.list_abit.age.error_text = None
                    self.list_abit.phone.error_text = None
                    self.list_abit.facultet.error_text = None
                    self.card.content = self.list_abit.card_for_change
                    self.list_abit.change.on_click = lambda e: self.db.change_abit(self.card, self.lv, self.page,
                                                                                       self.list_abit, phone)
                    self.page.add(self.card)
                    break
            self.page.update()


        def update_facultet(e, name_fac):
            self.page.close(self.list_facultet.update_or_delete)
            for i in range(len(self.list_facultet.tabel_facultet.rows)):
                if self.list_facultet.tabel_facultet.rows[i].cells[0].content.value == name_fac:
                    self.page.remove(self.lv)
                    self.list_facultet.name_fac.value = self.list_facultet.tabel_facultet.rows[i].cells[0].content.value
                    self.list_facultet.opisanie.value = self.list_facultet.tabel_facultet.rows[i].cells[1].content.value
                    self.list_facultet.name_fac.error_text = None
                    self.list_facultet.opisanie.error_text = None
                    self.card.content = self.list_facultet.card_for_change
                    self.list_facultet.change.on_click = lambda e: self.db.change_facultet(self.card, self.lv,
                                                                                           self.page, self.list_facultet,
                                                                                           name_fac, i)
                    self.list_abit.facultet.options = [ft.dropdown.Option(i[0]) for i in self.db.get_data_facultet()]

                    self.page.add(self.card)
                    break
            self.page.update()


        def update_exam(e, name_exam, date, aud):
            print(name_exam, date, aud)
            self.list_exam.name_exam.value = name_exam
            self.list_exam.date_exam.value = date
            self.list_exam.aud.value = aud
            self.card.content = self.list_exam.card_for_change
            self.list_exam.change.on_click = lambda e: self.db.change_exam(self.page, self.list_exam, name_exam, date, aud)
            self.list_exam.tabel_exam.rows = []
            for i in self.db.get_data_exam():
                self.list_exam.tabel_exam.rows.append(ft.DataRow(
                    cells=[ft.DataCell(ft.Text(j)) for j in i], on_select_changed=lambda e: open_card_exam(e)))
            self.lv.controls = [self.list_exam.tabel_exam]
            self.page.update()



        def open_on_facultet(e, fac):
            self.page.close(self.list_facultet.update_or_delete)
            self.list_abit.tabel_abiturient.rows = []
            for i in self.db.get_on_facultet(fac):
                self.list_abit.tabel_abiturient.rows.append(ft.DataRow(
                    cells=[ft.DataCell(ft.Text(j)) for j in i],
                    on_select_changed=lambda e: open_alert_dialog(e, e.control.cells[4].content.value)))
            self.lv.controls = [self.list_abit.tabel_abiturient]
            self.page.update()


        def find(e):
            if self.lv.controls == [self.list_abit.tabel_abiturient]:
                print(self.serch_str.value)
                list_for_find = list(self.db.find(self.serch_str.value))
                self.list_abit.tabel_abiturient.rows = []
                for i in list_for_find:
                    self.list_abit.tabel_abiturient.rows.append(ft.DataRow(
                        cells=[ft.DataCell(ft.Text(j)) for j in i],
                        on_select_changed=lambda e: open_alert_dialog(e, e.control.cells[4].content.value)))
                self.lv.controls = [self.list_abit.tabel_abiturient]
            if self.lv.controls == [self.list_exam.tabel_exam]:
                list_for_find = list(self.db.find_exam(self.serch_str.value))
                self.list_exam.tabel_exam.rows = []
                for i in list_for_find:
                    self.list_exam.tabel_exam.rows.append(ft.DataRow(
                        cells=[ft.DataCell(ft.Text(j)) for j in i], on_select_changed=lambda e: open_card_exam(e)))
                self.lv.controls = [self.list_exam.tabel_exam]

            if self.lv.controls == [self.list_facultet.tabel_facultet]:
                list_for_find = list(self.db.find_facultet(self.serch_str.value))
                self.list_facultet.tabel_facultet.rows = []
                for i in list_for_find:
                    self.list_facultet.tabel_facultet.rows.append(ft.DataRow(
                        cells=[ft.DataCell(ft.Text(j)) for j in i], on_select_changed=lambda e: open_alert_dialog_facultet(e, e.control.cells[0].content.value)))
                self.lv.controls = [self.list_facultet.tabel_facultet]
            self.page.update()


        self.page = page
        self.page.title = 'Приемная комиссия'
        self.page.theme_mode = 'dark'
        self.list_abit.btn_abit.on_click = lambda e: open(e)
        self.list_exam.btn_exam.on_click = lambda e: open(e)
        self.list_facultet.btn_fac.on_click = lambda e: open(e)
        self.list_abit.dr.on_click = lambda e: open_card(e)
        self.list_exam.dr.on_click = lambda e: open_card(e)
        self.list_facultet.dr.on_click = lambda e: open_card(e)
        self.list_abit.familiya.on_change= lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.name.on_change= lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.oth.on_change= lambda e:  self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.age.on_change= lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.facultet.on_change=lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.phone.on_change = lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.add_exam_abit1.on_change= lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.add_exam_abit2.on_change= lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.add_exam_abit3.on_change= lambda e: self.class_ex.validate(self.list_abit, self.page)
        self.list_abit.save_abit.on_click = lambda e: self.db.add_abiturient(self.list_abit, self.page)
        self.list_exam.save_exam.on_click = lambda e: self.db.add_exam(self.list_exam, self.page)
        self.list_facultet.name_fac.on_change = lambda e: self.class_ex.validate_facultet(self.list_facultet, self.page)
        self.list_facultet.opisanie.on_change = lambda e: self.class_ex.validate_facultet(self.list_facultet, self.page)
        self.list_facultet.save_fac.on_click = lambda e: self.db.add_facultet(self.list_facultet, self.page)
        self.list_exam.name_exam.on_change = lambda e: self.class_ex.validate_exam(self.list_exam, self.page)
        self.list_exam.date_exam.on_change = lambda e: self.class_ex.validate_exam(self.list_exam, self.page)
        self.list_exam.aud.on_change = lambda e: self.class_ex.validate_exam(self.list_exam, self.page)
        self.list_exam.delit_btn.on_click = lambda e: self.page.open(self.list_exam.quest)
        self.list_exam.quest.actions[1].on_click = lambda e: self.page.close(self.list_exam.quest)
        self.list_abit.quest.actions[1].on_click = lambda e: self.page.close(self.list_abit.quest)
        self.list_facultet.quest.actions[1].on_click = lambda e: self.page.close(self.list_facultet.quest)
        self.find_button.on_click = lambda e: find(e)
        add_nav = ft.Dropdown(hint_content=ft.Text('Добавить',
                                                   size=16,
                                                   color='#A0CAFD',
                                                   text_align=ft.TextAlign.CENTER),
                              height=50,
                              width=200,
                              border_radius=27,
                              text_size=16,
                              options=[self.list_abit.dr, self.list_exam.dr, self.list_facultet.dr])
        btns_nav = ft.Row([self.list_abit.btn_abit, self.list_exam.btn_exam, self.list_facultet.btn_fac, add_nav])
        self.page.add(btns_nav, ft.Row([self.othet, self.find_str]), self.lv)
        self.page.update()


app = Window()
ft.app(target=app.main)