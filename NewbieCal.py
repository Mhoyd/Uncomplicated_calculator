from tkinter import *

root = Tk()
root.title("Calculator")

#define function works  with btn
def Onscreen():
    msg1 = txt.get()
    msg2 = txt2.get()
    num1 = float(msg1)
    num2 = float(msg2)
    result_text.set(f"ผลลัพธ์ : {num1 + num2}")

def Closewindow():
    root.destroy()

def Add():
    msg1 = txt.get()
    msg2 = txt2.get()
    num1 = float(msg1)
    num2 = float(msg2)
    result_text.set(f"ผลลัพธ์ : {num1 + num2}")

def Subtract():
    msg1 = txt.get()
    msg2 = txt2.get()
    num1 = float(msg1)
    num2 = float(msg2)
    result_text.set(f"ผลลัพธ์ : {num1 - num2}")

def Multiply():
    msg1 = txt.get()
    msg2 = txt2.get()
    num1 = float(msg1)
    num2 = float(msg2)
    result_text.set(f"ผลลัพธ์ : {num1 * num2}")

def Divide():
    msg1 = txt.get()
    msg2 = txt2.get()
    num1 = float(msg1)
    num2 = float(msg2)
    if num2 != 0:
        result_text.set(f"ผลลัพธ์ : {num1 / num2}")
    else:
        result_text.set("ไม่สามารถหารด้วย 0 ได้")

Inform = Label(text=("เครื่องคิดเลข"),font=50, fg="black").place(x=125, y=155)

# Input for user
txt = StringVar()
Mytext = Entry(root, textvariable=txt).place(x=110, y=100)
txt2 = StringVar()
Mytext2 = Entry(root, textvariable=txt2).place(x=110, y=130)

# Create a StringVar for the result label
result_text = StringVar()

# Create a label to display the result
result_label = Label(textvariable=result_text, font=30, fg="black")
result_label.place(x=110, y=50)

# Buttons for arithmetic operations
plus = Button(root, text="บวก", fg="white", bg="black", font=1, command=Add)
plus.place(x=90, y=190)

minus = Button(root, text="ลบ", fg="white", bg="black", font=1, command=Subtract)
minus.place(x=135, y=190)

multi = Button(root, text="คูณ", fg="white", bg="black", font=1, command=Multiply)
multi.place(x=170, y=190)

divide = Button(root, text="หาร", fg="white", bg="black", font=1, command=Divide)
divide.place(x=210, y=190)

# Cancel Button

btn2 = Button(root, text="Cancel", fg="white", bg="black", font=25, command=Closewindow)
btn2.place(x=135, y=295)

# Define screen 
root.geometry("350x400+550+250")
root.mainloop()
