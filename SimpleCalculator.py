import tkinter as tk
from tkinter import *  
from tkinter import messagebox  


pencere = tk.Tk()
pencere.title("Simple calculator")
pencere.geometry("350x380")
pencere.config(bg="silver")


sonuç = tk.Label(pencere, text="Sonuç",width=30, height=2, justify="center")
sonuç.place(x=50,y=20)

sayi1 = tk.Entry(pencere,width=55,justify="right")
sayi1.place(x=10,y=80)

sayi2 = tk.Entry(pencere,width=55,justify="right")
sayi2.place(x=10,y=110)

def topla():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuç.configure(text=str(s1+s2))
        sayi1.focus()

def fark():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuç.configure(text=str(s1-s2))
        sayi1.focus()

def çarp():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuç.configure(text=str(s1*s2))
        sayi1.focus()


def böl():
    if sayi1.get().isdigit() and sayi2.get().isdigit():
        s1 = float(sayi1.get())
        s2 = float(sayi2.get())
        sonuç.configure(text=str(s1/s2))
        sayi1.focus()





def cık():
    cıkk = messagebox.askyesno("UYARI!", "Çıkmak istediğinize emin misiniz?")
    if cıkk == True:
       pencere.destroy()

tusx = tk.Button(pencere,text="x", width=7,command=cık,background="red")
tusx.place(x=290, y=0)


tus1 = tk.Button(pencere,text="+", width=10,command=topla,background="grey")
tus1.place(x=265, y=150)

tus2 = tk.Button(pencere,text="-", width=10,command=fark,background="grey")
tus2.place(x=265, y=200)


tus3 = tk.Button(pencere,text="x", width=10,command=çarp,background="grey")
tus3.place(x=265, y=250)

tus4 = tk.Button(pencere,text="/", width=10,command=böl,background="grey")
tus4.place(x=265, y=300)


def ekle(numara):
    if pencere.focus_get() == sayi2:
        sayi2.insert(END, str(numara))
    else:
        sayi1.insert(END, str(numara))

    



h1 = tk.Button(pencere,text="1", width=10,command=lambda: ekle(1))
h1.place(x=18, y=160)

h2 = tk.Button(pencere,text="2", width=10,command=lambda: ekle(2))
h2.place(x=18, y=190)

h3 = tk.Button(pencere,text="3", width=10,command=lambda: ekle(3))
h3.place(x=18, y=220)

h4 = tk.Button(pencere,text="4", width=10,command=lambda: ekle(4))
h4.place(x=18, y=250)

h5 = tk.Button(pencere,text="5", width=10,command=lambda: ekle(5))
h5.place(x=18, y=280)

h6 = tk.Button(pencere,text="6", width=10,command=lambda: ekle(6))
h6.place(x=120, y=160)

h7 = tk.Button(pencere,text="7", width=10,command=lambda: ekle(7))
h7.place(x=120, y=190)

h8 = tk.Button(pencere,text="8", width=10,command=lambda: ekle(8))
h8.place(x=120, y=220)

h9 = tk.Button(pencere,text="9", width=10,command=lambda: ekle(9))
h9.place(x=120, y=250)

h0 = tk.Button(pencere,text="0", width=10,command=lambda: ekle(0))
h0.place(x=120, y=280)
 






pencere.mainloop()