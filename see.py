
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk , Image
from tkinter import ttk
import os
from app import api2
from tkcalendar import DateEntry

class Ap:
    def __init__(self):
        self.path = ""

ap = Ap()
window = Tk()
window.geometry("460x360")
window.title(" OSC APP")
window.iconbitmap("img/favicon.ico")
window.resizable(0,0)
#image = Image.open("img/ORION.png")
#image = image.resize((300,140), Image.ANTIALIAS)
#imagen = ImageTk.PhotoImage(image)
#Label(window,image=imagen).place(x=70,y=80)

# def switchButtonState():
#     if (btn1['state'] == NORMAL):
#         btn1.config(state=DISABLED)
#     else:
#         print("Error")

def selectRoute():

    global path
    global route
    window.route = filedialog.askopenfilename(title='Selecciona la ruta')
    ap.path = window.route
    
    print(ap.path)

    extension = os.path.splitext(ap.path)[1]
    print(extension)


    if extension.lower() in [".csv"]:
        print(window.route)
        key = api_key.get()
        #cal = str(calendary.get())
        lugar = var_lugar.get()
        llamado = var_frecuencia.get()
        date = var_date.get()
        formato = var_format.get()
        print(key, lugar, llamado, date, formato) 
        #btn1.config(state=DISABLED)  
        Button(window, text = "Ejecutar",height="2", width="30",bg="#4DDEEC", command=lambda:api2(formato , key)).grid(row=23,column=2, padx=25)

        
        
    elif(len(ap.path) == 0 ):
        messagebox.showwarning('Invalided ',"Seleccione un archivo")
    else:
        messagebox.showerror('Error Invalided ',"Debes elegir un archivo compatible")







#def pv_power():
def form():
 
    return None

Label(text="PV POWER",fg="#F4FEFF", bg="darkblue", width="3000", height="2" ,font=("Corbel 17"))


btn1 = Button(window, text="Selecciona el csv con las coo",bg="gray", state=NORMAL,command=lambda:selectRoute()).grid(row=23,column=2, padx=25)#,switchButtonState()
# btn1.grid(row=3,column=1, padx=25)
# btn1.pack()
var_date = StringVar(window)
Label(window, text="Ingrese el dia a consultar:").grid(row=14,column=1, padx=25)
calendary=DateEntry(window, selectmode="day", textvariable=var_date).grid(row=20,column=1, padx=25)


var_lugar = StringVar(window)
Label(window, text="Zona horaria:").grid(row=6,column=2, padx=25)
var_lugar.set("Christmas Island (GMT+7)")
opciones_zona=['Christmas Island (GMT+7)', 'Perth (GMT+8)', 'Adelaide (GMT+9:30)', 'Kingston (GMT+11)']
#global eso
opcion_da_zona = OptionMenu(window, var_lugar, *opciones_zona)
opcion_da_zona.config(width=22)
# opcion_da_zona.pack()
opcion_da_zona.grid(row=7,column=2, padx=25)

es = Label(window, textvariable=str(var_lugar))

#llamado = str(eso)


var_frecuencia = StringVar(window)
Label(window, text="Frecuencia de llamados en minutos:").grid(row=13,column=2, padx=25)
var_frecuencia.set("10")
opciones_frecuencia=['10', '15', '20', '30']
# opciones_frecuencia.grid(row=2,column=1, padx=25)
# opciones_frecuencia.pack()
#global eso
opcion_frecuencia_llamados = OptionMenu(window, var_frecuencia, *opciones_frecuencia)
opcion_frecuencia_llamados.config(width=22)
opcion_frecuencia_llamados.grid(row=14,column=2, padx=25)


eso = Label(window, textvariable=var_frecuencia)
# # eso.pack()
# llamado = str(eso)

var_format = StringVar(window)
Label(window, text="Formato de los resultados:").grid(row=13,column=1, padx=25)
var_format.set("json")
opciones_data=['csv', 'json']

# global eso2
opcion = OptionMenu(window, var_format, *opciones_data)
opcion.grid(row=14,column=1, padx=25)
opcion.config(width=22)
# # opcion.pack()
# eso2 = Label(window, textvariable=var_data)

# # eso2.pack()
# formatter = str(eso2)




Label(text="Ingresa el API KEY:").grid(row=18, column=2, padx=25)

api_key = Entry(window, width=36)
api_key.grid(row=20,column=2, padx=25)

# api_key.pack()

# Label(text="").pack()

# def imprimir():

# solicitud=Button(window, text = "Solicitar",height="2", width="30",bg="gray",command=lambda:[form])
# solicitud.grid(row=23,column=2, padx=25)




# def solar_radiation():

#     Label(text="Solar Radiation : ",fg="#F4FEFF", bg="darkblue", width="300", height="2" ,font=("Corbel 17")).pack()

#     Label(text="Ingrea el angulo beta (°):").pack()
#     beta = Entry(window, width=36).pack()
#     Label(text="").pack()

#     Label(text="Ingresa el API KEY:").pack()
#     algo = Entry(window, width=36).pack()
#     Label(text="").pack()

#     # Label(text="Ingrea otra cosa:").pack()
#     # entru1=Entry(window, width=36).pack()
#     # Label(text="").pack()
#     print(algo)
#     Button(window, text = "Solicitar",height="2", width="30",bg="gray").pack() 


my_menu = Menu(window)

solcast = Menu(my_menu)


my_menu.add_cascade(menu=solcast, label='Solcast')
#solcast.add_command(label='Solar radiation', command=solar_radiation)

#solcast.add_command(label='PV power', command=pv_power)

# Creating a dropdown menu.

# def switchButtonState():
#     if (btn1['state'] == tk.NORMAL):
#         btn1.config(state=tk.DISABLED)
#     else:
#         print("Error")


#############################################################################################################################

Label(window)
window.config(menu=my_menu)
window.mainloop()