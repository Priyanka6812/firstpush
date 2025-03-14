from tkinter import *

root = Tk()
root.title ("Calculator")

root.geometry("600x460")
root.resizable(False, False)

#entry widget to display result
entry = Entry (root, font="Arial 40", bd=8, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4) 

#display the data in data entry widget
def display(num):
    value=entry.get()
    entry.delete(0, END)
    entry.insert(0, value + str(num))

#to clear entry widget
def clear():
    entry.delete(0, END)

#do the caculation part
def equal():
    try:
        result=str(eval(entry.get()))
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "ERROR")

#buttons for mathematical operations
button_9 = Button (root, text="9", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(9))
button_8 = Button (root, text="8", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(8))
button_7 = Button (root, text="7", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(7))
button_6 = Button (root, text="6", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(6))
button_5 = Button (root, text="5", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(5))
button_4 = Button (root, text="4", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(4))
button_3 = Button (root, text="3", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(3))
button_2 = Button (root, text="2", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(2))
button_1 = Button (root, text="1", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(1))
button_0 = Button (root, text="0", padx=20, pady=20, font="Arial 20 bold", command=lambda: display(0))

button_add = Button(root, text="+", padx=18, pady=20, font="Arial 20 bold", command=lambda: display('+'))
button_sub = Button(root, text="-", padx=21, pady=20, font="Arial 20 bold", command=lambda: display('-'))
button_mul = Button(root, text="*", padx=20, pady=20, font="Arial 20 bold", command=lambda: display('*'))
button_div = Button(root, text="/", padx=21, pady=20, font="Arial 20 bold", command=lambda: display('/'))

button_equal = Button(root, text="=", padx=20, pady=20, font="Arial 20 bold", command=equal)
button_clear = Button(root, text="C", padx=18, pady=20, font="Arial 20 bold", command=clear)

#arranging the buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_3.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)


root.mainloop()