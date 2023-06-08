from tkinter import *

#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 460
ALTURA = 220

#--------------------
# VENTANA PRINCIPAL
#--------------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")

#----------------------
# Frame de graficacion
#----------------------

frame_graficacion = Frame(ventana_principal)    
frame_graficacion.config(bg="green", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creacion canvas 

c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#--------------------
# frame controles
#--------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)



arco_1 = c.create_arc(0,0,BASE/2,ALTURA/2,start=180,extent=180, fill="red")
arco_2 = c.create_arc(0,0,BASE/2,ALTURA/2,start=0, extent=180, fill="white"   )

# molino
# desplegar ventana

ventana_principal.mainloop()












