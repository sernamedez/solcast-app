import solcast
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
import tkinter as tk


# class Ap:
#     def __init__(self):
#         self.path = ""
# ap = Ap()
window = Tk()
window.geometry("470x500")
window.title(" OSC APP")
window.iconbitmap("img/favicon.ico")
window.resizable(0,0)
image = Image.open("img/ORION.png")
image = image.resize((200,50), Image.ANTIALIAS)
imagen = ImageTk.PhotoImage(image)


def estimated_actuals(latitude, longitude, key):
    global data
    data = solcast.get_radiation_estimated_actuals(latitude, longitude, key).estimated_actuals
    print(type(data))


def open_file():
    if True:
        #text box
        Label(text="").grid()
        btn1.config(state=DISABLED)
        text_box = Text(window,  height=10, width=50, padx=10, pady=10)
        for y in data:
            ghi = y['ghi']
            period_end = y['period_end']
            info = f"{ghi} W/m2 - {period_end} (GMT+0)\n"
            print(info)
            text_box.insert(1.0,info) 
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid()


def selectRoute():

    if api_key.get() != "" and longitud.get() != "" and ll.get() != "":

        global latitud, long, key
        key = api_key.get()
        latitud = ll.get()
        long = longitud.get()
        print(key, long, latitud) 
        

    elif api_key.get() == "":
        messagebox.showwarning('Invalided ',"Ingresa el API KEY")

    elif longitud.get() == "":
        messagebox.showwarning('Invalided ',"Ingrese la longitud")

    elif ll.get() == "":
        messagebox.showwarning('Invalided ',"Ingrese la latitud")
    else:
        messagebox.showerror('Error Invalided ',"Error grave")


Label(text="SOLAR RADIATION",fg="#F4FEFF", bg="#2D61A6", width="40", height="2" ,font=("Arial 16")).grid(row=1, column=0)


Label(text="Ingresa la latitud:").grid(row=10, padx=25)
ll = Entry(window, width=36)
ll.grid(row=11, padx=25)
Label( text="Ingrsa la longitud:").grid(row=13, padx=25)
longitud = Entry(window, width=36)
longitud.grid(row=14, padx=25)
Label(text="Ingresa el API KEY:").grid(row=18, padx=25)
api_key = Entry(window, width=36)
api_key.grid(row=20, padx=25)


Label(text="").grid()
btn1 = tk.Button(window, image=imagen,state=NORMAL,height="50", width="217",bg="#9C9C9C", command=lambda:[selectRoute(), estimated_actuals( latitud, long, key),open_file()])
btn1.grid(row=23, padx=25)

Label(window)
window.config(menu=solcast)
window.mainloop()