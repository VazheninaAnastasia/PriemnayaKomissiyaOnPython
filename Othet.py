from fpdf import FPDF

from DataBase import DataBase


class Othet():
    def __init__(self):
        self.db = DataBase()

    def othet_exam(self):
        pdf = FPDF()
        pdf.set_font("Arial", size=12)
        pdf.add_page()

        col_width = pdf.w / 4.5
        row_height = pdf.font_size
        for row in list(self.db.get_data_exam()):
            pdf.cell(col_width, row_height, txt=(row[0] + ", " + row[1]), border=1)
            print(str(len(list(self.db.get_on_exam(row[0] + ", " + row[1])))))
            pdf.cell(col_width, row_height, txt=(str(len(list(self.db.get_on_exam(row[0] + ", " + row[1]))))), border=1)
            pdf.ln(row_height * 1)
        pdf.output('othet_for_exam.pdf')

    def othet_abiturient(self):
        pdf = FPDF()
        pdf.set_font("Arial", size=12)
        pdf.add_page()

        col_width = pdf.w / 7
        row_height = pdf.font_size
        for row in list(self.db.get_data_facultet()):
            pdf.cell(col_width, row_height * 1, txt=row[0], border=1)
            pdf.cell(col_width, row_height, txt=(str(len(list(self.db.get_on_facultet(row[0]))))), border=1)
            pdf.ln(row_height * 1)
        pdf.output('othet_for_abiturient.pdf')
