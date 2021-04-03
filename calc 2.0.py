from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('Калькулятор')  
rav = False
memory = ""
#логика калькулятора
def calc(key):
    str2 = "0123456789"
    if key == "=":
#исключаем написание букв
        str1 = "-+01234567789.*/"
        if calc_entry.get()[0] not in str1:
            calc_entry.delete(0, END)
            calc_entry.insert(END, "Первый символ не число!")
            messagebox.showerror("Ошибка!", "Вы ввели не число!")
#счёт
        try:
            result = eval(calc_entry.get())
            calc_entry.delete(0, END)
            if (result % 1 == 0):
                result = round(result)
            calc_entry.insert(END, str(result))
            global rav
            rav = True
        except:
            calc_entry.delete(0, END)
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror("Ошибка!","Проверь правильность написания!")
#очистить поле
    elif key == "C":
        calc_entry.delete(0, END)
#удалить последний символ
    elif key == "del":
        calc_entry.delete(len(calc_entry.get())-1, END) 
#память
    elif key == "M":
        global memory
        str1 = "-+01234567789.*/" 
        if calc_entry.get()[0] not in str1:
            calc_entry.delete(0, END)
            calc_entry.insert(END, "Первый символ не число!")
            messagebox.showerror("Ошибка!", "Вы ввели не число!")
#счёт
        try:
            temp = eval(calc_entry.get())
            if (temp % 1 == 0):
                temp = round(temp) 
            memory = str(temp)[:10]
        except:
            calc_entry.delete(0, END)
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror("Ошибка!","Проверь правильность написания!")
        memory_label.config(text = "M: " + memory)
    elif key == "M+":
        if memory != "0":
            calc_entry.insert(END,"+" + memory)    
    elif key == "M-":
        if memory != "0":
            calc_entry.insert(END,"-" + memory) 
    elif key == "MC":
        memory = "0"
        memory_label.config(text = "M: " + memory) 
#смена +/-
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "-" or key == "/" or key == "*" or key == "+":
        if calc_entry.get()[len(calc_entry.get())-1] in str2:
                calc_entry.insert(END, key)
                rav = False
    elif key == ".":
        x1 = calc_entry.get().rfind("+")
        x2 = calc_entry.get().rfind("-")
        x3 = calc_entry.get().rfind("*")
        x4 = calc_entry.get().rfind("/")
        x = max(x1, x2, x3, x4)
        if x == -1:
            x = 0
        if (calc_entry.get()[x:] != ""):
            if key not in calc_entry.get()[x:]:
                calc_entry.insert(END, key)
                rav = False
    else:
        if not rav:
            calc_entry.insert(END, key)
        else:
            calc_entry.delete(0, END)
            calc_entry.insert(END, key)
            rav = False

#создаем все кнопки
bttn_list = [
         "M", "M+", "M-", "MC",
         "7", "8", "9", "+", "-",
         "4", "5", "6", "*", "/",
         "1", "2", "3", "-/+", "=",
         "0", ".", "C", "del"
             ]

r = 1
c = 1

for i in bttn_list:
    action =  lambda x = i: calc(x)
    if i == '=':
        ttk.Button = Button(root, text = i, command = action, bg = '#a3b8cf', width = 10, height = 7, bd = 3) 
        ttk.Button.grid(row = r, column = c, rowspan = 2)      
    else:
        ttk.Button = Button(root, text = i, command = action, bg = '#a3b8cf', width = 10, height = 3, bd = 3) 
        ttk.Button.grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 40, bd = 5, font = 10, justify = RIGHT)
calc_entry.grid(row = 0, column = 0, columnspan = 5)
#значение памяти
memory_label = Label(root, text = "M: 0", width = 10)
memory_label.grid(row = 1, column = 0)
#im = PhotoImage(file='Tree1.gif')
#memory_label.image = im
root.mainloop()
