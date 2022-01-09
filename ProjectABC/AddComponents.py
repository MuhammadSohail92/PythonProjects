import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import LoginPage as lp
import seconPage as sp
import thirdPage as tp
import dbPage as dp


def AddCompon():
    window = tk.Tk()
    window.resizable(0, 0)
    window.configure(bg="deep sky blue")
    window.title("Add Components")
    l1 = tk.Label(window, text="Rack#:", font=("Arial", 15), bg="deep sky blue")
    l1.place(x=10, y=10)
    t1 = tk.Entry(window, width=30, bd=5)
    t1.place(x=200, y=10)

    l2 = tk.Label(window, text="Description:", font=("Arial", 15), bg="deep sky blue")
    l2.place(x=10, y=60)
    t2 = tk.Entry(window, width=50, bd=5)
    t2.place(x=200, y=60)

    l3 = tk.Label(window, text="Qty:", font=("Arial", 15), bg="deep sky blue")
    l3.place(x=10, y=110)
    t3 = tk.Entry(window, width=30, show="*", bd=5)
    t3.place(x=200, y=110)

    def Add():
        if t1.get() != "" or t2.get() != "" or t3.get() != "":
            # f.write(t1.get() + "," + t2.get() + "\n")
            dp.addComponents(t1.get(),t2.get(),t3.get())
            messagebox.showinfo("Info", "Your addition successful!!")

        else:
            messagebox.showinfo("Error", "Please fill the complete field!!")

    b1 = tk.Button(window, text="Add Detail", font=("Arial", 15), bg="#ffc22a", command=Add)
    b1.place(x=170, y=150)

    window.geometry("470x220")
    window.mainloop()