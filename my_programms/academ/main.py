from email import encoders
from email.mime.base import MIMEBase
import smtplib
import os
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



me = 'mitlinleonid@gmail.com'
me2 = 'mitlinleonid@liceyklassic.ru'
password = 'CikjG6NiHtmawG1986'
password_2 = 'sonar078111986'
password_1 = 'pcxvmplounbgtfju'

email_getter = 'mitlinleonid@yandex.ru'

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(me2, password_2)

msg = MIMEMultipart()
msg["Subject"] = "Тут тема сообщени23232я"
msg.attach(MIMEText("Привет, это я сно232323ва и снова"))

file = "C:\\my_project\\algorithms\\my_programms\\academ\\Это приказ.docx"
filename = os.path.basename(file)
ftype, encoding = mimetypes.guess_type(file)
file_tupe, subtype = ftype.split("/")

with open(file, "rb") as f:
    file1 = MIMEBase(file_tupe, subtype)
    file1.set_payload(f.read())
    encoders.encode_base64(file1)

file1.add_header('content-disposition', 'attachment', filename=filename)

msg.attach(file1)


smtp_server.sendmail(me2, me2, msg.as_string())


import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
import my_data

def template_prikaz():
    doc = DocxTemplate("template_prikaz.docx")
    data_prikaza = ent_date_prikaz.get()
    number = com_period_number.get()
    period = com_period.get()
    student = com_student.get()
    klass = com_klass.get()
    last_name_rod = ent_last_name_rod.get()
    first_name_rod = ent_first_name_rod.get()
    predmet = com_predmet.get()
    date_exam = ent_date_exam.get()
    klass_ruk_dat = com_klass_ruk_dat.get()
    document_return = ent_document_return.get()
    teacher_dat = com_teacher_dat.get()
    predmet_rod = com_predmet_rod.get()
    klass_ruk = com_klass_ruk.get()
    teacher = com_teacher.get()
    if klass_ruk == teacher:
        teacher = ""
    first_name = ent_first_name.get()
    last_name = ent_last_name.get()
    context = { 'data_prikaza' : data_prikaza,
                'number' : number, 
                'period' : period,
                'student' : student,
                'klass' : klass,
                'last_name_rod' : last_name_rod,
                'first_name_rod' : first_name_rod,
                'predmet' : predmet,
                'date_exam' : date_exam,
                'klass_ruk_dat' : klass_ruk_dat,
                'document_return' : document_return,
                'teacher_dat' : teacher_dat,
                'predmet_rod' : predmet_rod,
                'klass_ruk' : klass_ruk,
                'teacher' : teacher}
    doc.render(context)
    name_file = 'приказ_'+last_name+'_'+first_name+'_'+klass+'_'+predmet+'_'+number+'_'+period+'_'+data_prikaza+'.docx'
    doc.save(name_file)

def template_grafik():
    doc = DocxTemplate("template_grafik.docx")
    data_prikaza = ent_date_prikaz.get()
    number = com_period_number.get()
    period = com_period.get()
    student = com_student.get()
    klass = com_klass.get()
    predmet_rod = com_predmet_rod.get()
    teacher = com_teacher.get()
    first_name = ent_first_name.get()
    last_name = ent_last_name.get()
    predmet = com_predmet.get()
    obuch = ''
    if student == 'ученика':
        obuch = 'Обучающийся'
    else:
        obuch = 'Обучающаяся'
    context = { 'number' : number, 
                'period' : period,
                'student' : student,
                'klass' : klass,
                'predmet_rod' : predmet_rod,
                'teacher' : teacher,
                'first_name' : first_name,
                'last_name' : last_name,
                'obuch' : obuch}
    doc.render(context)
    name_file = 'График индивидуальных занятий_'+last_name+'_'+first_name+'_'+klass+'_'+predmet+'_'+number+'_'+period+'_'+data_prikaza+'.docx'
    doc.save(name_file)


def temlate_protokol():
    doc = DocxTemplate("template_protokol.docx")
    data_prikaza = ent_date_prikaz.get()
    number = com_period_number.get()
    period = com_period.get()
    student = com_student.get()
    klass = com_klass.get()
    last_name_rod = ent_last_name_rod.get()
    first_name_rod = ent_first_name_rod.get()
    predmet = com_predmet.get()
    date_exam = ent_date_exam.get()
    context = { 'number' : number, 
                'period' : period,
                'student' : student,
                'klass' : klass,
                'last_name_rod' : last_name_rod,
                'first_name_rod' : first_name_rod,
                'predmet' : predmet,
                'date_exam' : date_exam}
    doc.render(context)
    name_file = 'протокол ликвидации академической задолженности_'+last_name_rod+'_'+first_name_rod+'_'+predmet+'_'+number+'_'+period+'_'+data_prikaza+'.docx'
    doc.save(name_file)

def templates_all():
    template_grafik()
    temlate_protokol()
    template_prikaz()

windows = tk.Tk()
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)

frm_form.pack()
# Выпадающий список ученика/ученицы
lbl_student = tk.Label(master=frm_form, text="кого:")
com_student = ttk.Combobox(master=frm_form, width=50, values=['ученика', 'ученицы'])
lbl_student.grid(row=0, column=0, sticky='e')
com_student.grid(row=0, column=1)

# Создает ярлык и текстовок поле для ввода имени.
lbl_first_name = tk.Label(master=frm_form, text="Имя:")
ent_first_name = tk.Entry(master=frm_form, width=50)
# Использует менеджер геометрии grid для размещения ярлыка и
# однострочного поля для ввода текста в первый и второй столбец
# первой строки сетки.
lbl_first_name.grid(row=1, column=0, sticky="e")
ent_first_name.grid(row=1, column=1)
 
# Создает ярлык и текстовок поле для ввода фамилии.
lbl_last_name = tk.Label(master=frm_form, text="Фамилия:")
ent_last_name = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на вторую строку сетки
lbl_last_name.grid(row=2, column=0, sticky="e")
ent_last_name.grid(row=2, column=1)
 
# Создает ярлык и текстовок поле для ввода имени в родительном падеже.
lbl_first_name_rod = tk.Label(master=frm_form, text="Имя в род.:")
ent_first_name_rod = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на третьей строке сетки.
lbl_first_name_rod.grid(row=3, column=0, sticky="e")
ent_first_name_rod.grid(row=3, column=1)
 
# Создает ярлык и текстовок поле для ввода фамилии в родительном падеже.
lbl_last_name_rod = tk.Label(master=frm_form, text="Фамилия в род.:")
ent_last_name_rod = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на четвертой строке сетки.
lbl_last_name_rod.grid(row=4, column=0, sticky="e")
ent_last_name_rod.grid(row=4, column=1)

# Создает ярлык и выпадающий список для ввода номера класса.
lbl_klass = tk.Label(master=frm_form, text="Класс:")
com_klass = ttk.Combobox(master=frm_form, width=50, values=[5, 6, 7, 8, 9, 10, 11])
# Размещает виджеты на пятой строке сетки.
lbl_klass.grid(row=5, column=0, sticky="e")
com_klass.grid(row=5, column=1)

# Создает ярлык и выпадающий список для ввода предмета.
lbl_predmet = tk.Label(master=frm_form, text="Предмет:")
com_predmet = ttk.Combobox(master=frm_form, width=50, values=my_data.predmet)
# Размещает виджеты на шестой строке сетки.
lbl_predmet.grid(row=6, column=0, sticky="e")
com_predmet.grid(row=6, column=1)

# Выпадающий список период четверть/полугодие
lbl_period = tk.Label(master=frm_form, text="Период:")
com_period = ttk.Combobox(master=frm_form, width=50, values=['четверть', 'полугодие'])
lbl_period.grid(row=7, column=0, sticky='e')
com_period.grid(row=7, column=1)

# Создает ярлык и выпадающий список для ввода номера периода.
lbl_period_number = tk.Label(master=frm_form, text="Номер периода:")
com_period_number = ttk.Combobox(master=frm_form, width=50, values=[1, 2, 3, 4])
# Размещает виджеты на восьмой строке сетки.
lbl_period_number.grid(row=8, column=0, sticky="e")
com_period_number.grid(row=8, column=1)

# Создает ярлык и выпадающий список для ввода классного руководителя.
lbl_klass_ruk = tk.Label(master=frm_form, text="Классный руководитель:")
com_klass_ruk = ttk.Combobox(master=frm_form, width=50, values=my_data.teacher)
# Размещает виджеты на девятой строке сетки.
lbl_klass_ruk.grid(row=9, column=0, sticky="e")
com_klass_ruk.grid(row=9, column=1)

# Создает ярлык и выпадающий список для ввода классного руководителя в дательном падеже.
lbl_klass_ruk_dat = tk.Label(master=frm_form, text="Классный руководитель в дат:")
com_klass_ruk_dat = ttk.Combobox(master=frm_form, width=50, values=my_data.teacher_dat)
# Размещает виджеты на десятой строке сетки.
lbl_klass_ruk_dat.grid(row=10, column=0, sticky="e")
com_klass_ruk_dat.grid(row=10, column=1)

# Создает ярлык и выпадающий список для ввода учителя.
lbl_teacher = tk.Label(master=frm_form, text="Учитель:")
com_teacher = ttk.Combobox(master=frm_form, width=50, values=my_data.teacher)
# Размещает виджеты на одинадцатой строке сетки.
lbl_teacher.grid(row=11, column=0, sticky="e")
com_teacher.grid(row=11, column=1)

# Создает ярлык и выпадающий список для ввода учителя в дательном падеже.
lbl_teacher_dat = tk.Label(master=frm_form, text="Учитель в дат:")
com_teacher_dat = ttk.Combobox(master=frm_form, width=50, values=my_data.teacher_dat)
# Размещает виджеты на двенадцатой строке сетки.
lbl_teacher_dat.grid(row=12, column=0, sticky="e")
com_teacher_dat.grid(row=12, column=1)

# Создает ярлык и выпадающий список для ввода предмета в родительном падеже.
lbl_predmet_rod = tk.Label(master=frm_form, text="Предмет в род:")
com_predmet_rod = ttk.Combobox(master=frm_form, width=50, values=my_data.predmet_2)
# Размещает виджеты на тринадцатой строке сетки.
lbl_predmet_rod.grid(row=13, column=0, sticky="e")
com_predmet_rod.grid(row=13, column=1)

# Создает ярлык и текстовок поле для ввода даты пересдачи.
lbl_date_exam = tk.Label(master=frm_form, text="Дата пересдачи:")
ent_date_exam = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на 14 строке сетки.
lbl_date_exam.grid(row=14, column=0, sticky="e")
ent_date_exam.grid(row=14, column=1)
 
# Создает ярлык и текстовок поле для ввода Даты сдачи документа
lbl_document_return = tk.Label(master=frm_form, text="Дата сдачи документов:")
ent_document_return = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на 15 строке сетки.
lbl_document_return.grid(row=15, column=0, sticky="e")
ent_document_return.grid(row=15, column=1)
 
# Создает ярлык и текстовок поле для ввода даты приказа.
lbl_date_prikaz = tk.Label(master=frm_form, text="Дата приказа:")
ent_date_prikaz = tk.Entry(master=frm_form, width=50)
# Размещает виджеты на восьмой строке сетки.
lbl_date_prikaz.grid(row=16, column=0, sticky="e")
ent_date_prikaz.grid(row=16, column=1)
 
# Создает новую рамку `frm_buttons` для размещения
# кнопок "Отправить" и "Очистить". Данная рамка заполняет
# все окно в горизонтальном направлении с
# отступами в 5 пикселей горизонтально и вертикально.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
 
# Создает кнопку "Отправить" и размещает ее
# справа от рамки `frm_buttons`.
btn_submit = tk.Button(master=frm_buttons, text="Отправить")
btn_submit.config(command=templates_all)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)
windows.mainloop()