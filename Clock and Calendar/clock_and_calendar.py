from tkinter import *
from tkinter import ttk
from time import strftime
from tkcalendar import Calendar

root = Tk()
root.title("Clock & Calendar")
root.configure(bg="beige")

def update_time():
    string = strftime('%H:%M:%S %p')
    time_label.config(text=string)
    time_label.after(1000, update_time)

def update_calendar():
    year = int(strftime('%Y'))
    month = int(strftime('%m'))
    cal_frame = Frame(root, bg="beige")
    cal = Calendar(
        cal_frame,
        selectmode="day",
        background='brown',
        foreground='white',
        bordercolor='black',
        headersbackground='beige',
        normalbackground='beige',
        normalforeground='black',
        weekendbackground='beige',
        weekendforeground='light grey',
        othermonthbackground='black',
        othermonthforeground='gray',
        font=("Poppins", 15),
        showothermonthdays=False,
        selectbackground='beige',
        selectforeground='black'
    )
    cal.pack()
    cal_frame.pack(anchor='center')

time_label = Label(root, font=("Futura", 60), background="beige", foreground="brown")
time_label.pack(anchor='center', pady=20)

update_time()
update_calendar()

root.mainloop()