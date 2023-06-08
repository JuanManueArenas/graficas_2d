from tkinter import *
import random
#---------------------
# VARIABLES GLOBALES
#--------------------

BASE = 460
ALTURA = 220
RADIO = 50


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


    # Generar 100 circulos de 20 de radio y color y posicion aleatoria sin salirse del canvas
for i in range(100):
        #generar color aleatorio
    color = "#"
    for i in range(6):
        color = color + random.choice("0123456789ABCDEF")
    #generar color aleatorio 
    radio = random.randint(5,25)

    x = random.randint(0,  BASE-2*radio)
    y = random.randint(0, ALTURA-2*radio)         
         
       
    #dibujamos el circulo
    circulo = c.create_arc(x,y,x+2*radio,y+2*radio, start=50 ,extent= 300,fill = color)


    img_nave = PhotoImage(file="img/nave2.png")
    nave = c.create_image(BASE/2,ALTURA/2,image=img_nave)

#barra de desplazamiento


#--------------------
# frame controles
#--------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

linea_central_horizontal = c.create_line(0,ALTURA/2,BASE,ALTURA/2, fill="red")
linea_central_vertical = c.create_line(BASE/2,0,BASE/2,ALTURA, fill= "red")

ventana_principal.mainloop()