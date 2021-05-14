
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------
from tkinter import *
import math

def disk(a, b, c):                       #Формула дискриминанта
    D = b**2 - (4*a*c)
    if D > 0:
        x1 = round((-b + math.sqrt(D))/(2*a),1)
        x2 = round((-b - math.sqrt(D))/(2*a),1)
        return x1,x2
    elif D == 0:
        x = (-b)/(2*a)
        return x, "Один корень", x
    else:
        return "Корней нет.", ""


def show_otvet(event):
	global input_a
	global input_b
	global input_c
	global answer

	x1,x2 = disk(float(input_a.get()),float(input_b.get()),float(input_c.get()))
	answer.config(text="Ответ = " + str(x1) + " ; " + str(x2))


window = Tk()
window.title("Калькулятор уравнений")
window.geometry("1920x1080") 

l = Label(window, text="Решение квадратного уравнения", font="Arial 24", bg="lightblue", bd=5, fg="black" )
l.pack(side=TOP)
knopka = Button(window,text="Решить", fg="black", bg="lightgreen", font="Arial 40", width=10)
input_a = Entry(window, width=4, bd=10,font="Arial 20", bg="lightblue")
input_b = Entry(window, width=4, bd=10,font="Arial 20", bg="lightblue")
input_c = Entry(window, width=4, bd=10,font="Arial 20", bg="red")
window.geometry('400x600')
input_a.pack(side=LEFT)
l = Label(window, text="x * * 2+",width=15,fg="green",bd=20,font="Arial 20" )
l.pack(side=LEFT)
input_b.pack(side=LEFT)
l = Label(window, text="x +" ,width=15,fg="green",bd=20,font="Arial 20")
l.pack(side=LEFT)
input_c.pack(side=LEFT)
l = Label(window, text=" = 0" ,width=15,fg="green",bd=20,font="Arial 20")
l.pack(side=LEFT)



answer = Label(window, text="Ответ: x1/x2 = ", font="Arial 24")
answer.pack(side=LEFT, anchor=SW)


knopka.pack(side=LEFT)
knopka.bind("<Button-1>",func=show_otvet)
window.mainloop()


