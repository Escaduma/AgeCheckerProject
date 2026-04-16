from tkinter import *
from tkinter import messagebox
from age_checker import check_age

def handle_check_age():
    age=int(age_entry.get())
    result = check_age(age)
    result_label.config(text=result)

root=Tk()
root.title("Age Checker")
root.geometry("300x220")

title_label=Label(root, text="Age Checker")
title_label.pack(pady=10)

age_label=Label(root, text="Enter your age: ")
age_label.pack()

age_entry=Entry(root)
age_entry.pack()

check_button=Button(root, text="Check Age", command=handle_check_age)
check_button.pack(pady=10)

result_label=Label(root, text="")
result_label.pack()

root.mainloop()

#It helps to use the variables of the function made.
#For me is like make the GUI making it a variable in order to use it.
#It helps to maintain the GUI running
#A label it is just like a title you cannot write or dor somethina and in the entry you can write text
#A pack helps to put everithing together in one window
#It returns the entry made to insert soemthing 
#because the program needs to recognize the text put it in a number
#Because we don't want to print the function, like running it in the GUI, we just want to make it in the background
#A value Error is displayed in the terminal
