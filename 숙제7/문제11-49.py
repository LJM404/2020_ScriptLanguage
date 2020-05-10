import random
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("")
root.geometry("180x210")
root.resizable(False, False)

o_image = PhotoImage(file="image/o.gif") # 60 x 60 size
x_image = PhotoImage(file="image/x.gif") # 60 x 60 size

tables_value = []
tables = []

def pressReset():
    tables_value = [random.randint(0, 1) for n in range(9)]
    for i in range(3):
        for j in range(3):
            if tables_value[i * 3 + j] == 0:
                tables.append(ttk.Label(root, image=o_image))
            else:
                tables.append(ttk.Label(root, image=x_image))
            tables[-1].place(x=i*60, y=j*60)
    root.update()

reset_button = ttk.Button(root, text="다시생성", command=pressReset)
reset_button.place(x=45, y=185)

pressReset()

# run
root.mainloop()