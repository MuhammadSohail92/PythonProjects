import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import LoginPage as lp
import thirdPage as tp
import dbPage as dp
import AddComponents as adc


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #        load = Image.open("img2.jpg")
        #        photo = ImageTk.PhotoImage(load)
        #        label = tk.Label(self, image=photo)
        #        label.image = photo
        #        label.place(x=0, y=0)

        LblLoguser = tk.Label(self, text="abc", font=("Arial Bold", 15), bg='ivory')
        LblLoguser.place(x=50, y=20)
        if dp.isSqlite3Db('appdb.db'):
            dp.connectdb()
            LblLoguser.config(text=dp.getsessionuser())

        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(tp.ThirdPage))
        Button.place(x=650, y=450)

        B2 = tk.Button(self, text="Add Components", bg="dark orange", font=("Arial", 15), command=adc.AddCompon())
        B2.place(x=150, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(lp.loginform))
        Button.place(x=100, y=450)
