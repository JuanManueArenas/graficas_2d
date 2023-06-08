from tkinter import *
import random
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

linea_central_horizontal = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="red")
linea_central_vertical = c.create_line(BASE/2,0,BASE/2,ALTURA, fill= "red")

color = "#"
for i in range(6):
    color = color + random.choice("0123456789ABCDEF")

casa_triangular = c.create_polygon(BASE/2,ALTURA/2,BASE/2+20,ALTURA,BASE/2,ALTURA,BASE/2-20,ALTURA/2+110, fill="cyan")
base = c.create_rectangle(BASE/2-100,ALTURA/2+80,BASE/2+100,ALTURA/2+110, fill="brown")
arco_1 = c.create_arc(BASE/2-60,ALTURA/2+30,BASE/2+60,ALTURA/2-30,start=90,extent=60, fill=color)
arco_2 = c.create_arc(BASE/2-60,ALTURA/2+30,BASE/2+60,ALTURA/2-30,start=180,extent=60, fill="red")
arco_3 = c.create_arc(BASE/2-60,ALTURA/2+30,BASE/2+60,ALTURA/2-30,start=270,extent=60, fill="white")
arco_4 = c.create_arc(BASE/2-60,ALTURA/2+30,BASE/2+60,ALTURA/2-30,start=360,extent=60, fill="red")

ventana_principal.mainloop()
