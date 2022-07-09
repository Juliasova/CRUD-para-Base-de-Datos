import tkinter
from tkinter import *
from tkmacosx import *

raiz = tkinter.Tk()
raiz.title('Ejemplo')

barramenu = tkinter.Menu(raiz)
raiz.config(menu = barramenu)

bbddmenu = tkinter.Menu(barramenu,tearoff=0)
borrarmenu = tkinter.Menu(barramenu,tearoff=0)
ayudamenu = tkinter.Menu(barramenu,tearoff=0)

barramenu.add_cascade(label='BBDD', menu=bbddmenu)
barramenu.add_cascade(label='Limpiar', menu=borrarmenu)
barramenu.add_cascade(label='Ayuda', menu=ayudamenu)

framecampos=Frame(raiz)
framecampos.pack()

legajo=StringVar()
alumno=StringVar()
email=StringVar()
calificacion=DoubleVar()
grado=IntVar()
escuela=StringVar()
localidad=StringVar()
provincia=StringVar()

legajo_input=Entry(framecampos, textvariable=legajo,bg='#E69A8D')
legajo_input.grid(row=0,column=1,padx=10,pady=10)

alumno_input=Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1,column=1,padx=10,pady=10)

email_input=Entry(framecampos, textvariable=email)
email_input.grid(row=2,column=1,padx=10,pady=10)

calificacion_input=Entry(framecampos, textvariable=legajo)
calificacion_input.grid(row=3,column=1,padx=10,pady=10)

grado_input=Entry(framecampos, textvariable=grado)
grado_input.grid(row=4,column=1,padx=10,pady=10)

escuela_input=Entry(framecampos, textvariable=escuela)
escuela_input.grid(row=5,column=1,padx=10,pady=10)

localidad_input=Entry(framecampos, textvariable=localidad)
localidad_input.grid(row=6,column=1,padx=10,pady=10)

provincia_input=Entry(framecampos, textvariable=provincia)
provincia_input.grid(row=7,column=1,padx=10,pady=10)

legajolabel=Label(framecampos, text='Legajo: ',font='Calibri 18 bold')
legajolabel.grid(row=0,column=0, sticky='e', padx=10,pady=10)

nombrelabel=Label(framecampos, text='Nombre: ',font='Verdana 18 bold')
nombrelabel.grid(row=1,column=0, sticky='e', padx=10,pady=10)

emaillabel=Label(framecampos, text='Email: ')
emaillabel.grid(row=2,column=0, sticky='e', padx=10,pady=10)

calificacionlabel=Label(framecampos, text='Calificacion: ')
calificacionlabel.grid(row=3,column=0, sticky='e', padx=10,pady=10)

gradolabel=Label(framecampos, text='Grado: ')
gradolabel.grid(row=4,column=0, sticky='e', padx=10,pady=10)

escuelalabel=Label(framecampos, text='Escuela: ')
escuelalabel.grid(row=5,column=0, sticky='e', padx=10,pady=10)

localidadlabel=Label(framecampos, text='Localidad: ')
localidadlabel.grid(row=6,column=0, sticky='e', padx=10,pady=10)

provincialabel=Label(framecampos, text='Provincia: ')
provincialabel.grid(row=7,column=0, sticky='e', padx=10,pady=10)

framebotones=Frame(raiz)
framebotones.pack()

boton_crear=Button(framebotones, text='Crear',bg='#ADEFD1')
boton_crear.grid(row=0,column=0,sticky='e',padx=10,pady=10)

boton_leer=Button(framebotones, text='Leer')
boton_leer.grid(row=0,column=1,sticky='e',padx=10,pady=10)

boton_actualizar=Button(framebotones, text='Actualizar')
boton_actualizar.grid(row=0,column=2,sticky='e',padx=10,pady=10)

boton_borrar=Button(framebotones, text='Borrar')
boton_borrar.grid(row=0,column=3,sticky='e',padx=10,pady=10)

framecopy=Frame(raiz)
framecopy.pack()

copylabel=Label(framecopy,text='Big Data 2022 - Comision 22045')
copylabel.grid(row=0,column=0,sticky='e',padx=10,pady=10)

raiz.mainloop()