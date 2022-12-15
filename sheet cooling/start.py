import main_edited as main
from tkinter import *
from tkinter import ttk, Tk, Frame, Menu
import tkinter as tk
from PIL import Image, ImageTk

#chama main
def chama(*args):
    m1=matg1var.get()
    m2=matg2var.get()
    m3=matg3var.get()
    m4=matg4var.get()
    f1=flug1var.get()
    f2=flug2var.get()
    f3=flug3var.get()
    f4=flug4var.get()
    ti1=Tempming1.get()
    ti2=Tempming2.get()
    ti3=Tempming3.get()
    ti4=Tempming4.get()
    ts1=Tempmaxg1.get()
    ts2=Tempmaxg2.get()
    ts3=Tempmaxg3.get()
    ts4=Tempmaxg4.get()
    tf1=Tempambg1.get()
    tf2=Tempambg2.get()
    tf3=Tempambg3.get()
    tf4=Tempambg4.get()
    vs1=estg1.get()
    if vs1 == 1:
        s1=txtg1.get()
    else:
        s1=formg1.get()
    vs2=estg2.get()
    if vs2 == 1:
        s2=txtg2.get()
    else:
        s2=formg2.get()
    vs3=estg3.get()
    if vs3 == 1:
        s3=txtg3.get()
    else:
        s3=formg3.get()
    vs4=estg4.get()
    if vs4 == 1:
        s4=txtg4.get()
    else:
        s4=formg4.get()

    if Tempxvar.get()==True :
        ts2=ts1
        ts3=ts1
        ts4=ts1
    if Tempmvar.get() == True :
        ti2=ti1
        ti3=ti1
        ti4=ti1
    if estvar.get() == True :
        vs2=vs1
        vs3=vs1
        vs4=vs1
        s2=s1
        s3=s1
        s4=s1
    if matvar.get() == True :
        m2=m1
        m3=m1
        m4=m1
    if fluvar.get() == True :
        f2=f1
        f3=f1
        f4=f1
    if Tempavar.get() == True :
        tf2=tf1
        tf3=tf1
        tf4=tf1

    main.simula(m1,m2,m3,m4,f1,f2,f3,f4,float(ti1),float(ti2),float(ti3),float(ti4),float(ts1),float(ts2),float(ts3),float(ts4),float(tf1),float(tf2),float(tf3),float(tf4),vs1,s1,vs2,s2,vs3,s3,vs4,s4)


#defs show/hide
def updatecheck():
    if Tempxvar.get()==True and Tempmvar.get() == True and estvar.get() == True and matvar.get() == True and fluvar.get() == True and Tempavar.get() == True:
        titulog1.configure(text="Chapas:", font=('Oswald',14))
        titulog2.grid_forget()
        titulog3.grid_forget()
        titulog4.grid_forget()
    else:
        titulog1.configure(text="Chapa 1:", font=('Oswald',14))
        titulog2.grid(column=0, row=5, sticky=(W))
        titulog3.grid(column=0, row=7, sticky=(W))
        titulog4.grid(column=0, row=9, sticky=(W))

    if Tempavar.get() == True:
        tempatitg2.grid_forget()
        Tempag2.grid_forget()

        tempatitg3.grid_forget()
        Tempag3.grid_forget()

        tempatitg4.grid_forget()
        Tempag4.grid_forget()
    else:
        tempatitg2.grid(column=2, row=0, pady=5)
        Tempag2.grid(column=3, row=0 )
        
        tempatitg3.grid(column=2, row=0, pady=5)
        Tempag3.grid(column=3, row=0 )

        tempatitg4.grid(column=2, row=0, pady=5)
        Tempag4.grid(column=3, row=0 )

    if Tempxvar.get() == True:
        tempxtitg2.grid_forget()
        Tempxg2.grid_forget()

        tempxtitg3.grid_forget()
        Tempxg3.grid_forget()

        tempxtitg4.grid_forget()
        Tempxg4.grid_forget()
    else:
        tempxtitg2.grid(column=2, row=1, pady=5)
        Tempxg2.grid(column=3, row=1 )

        tempxtitg3.grid(column=2, row=1, pady=5)
        Tempxg3.grid(column=3, row=1 )

        tempxtitg4.grid(column=2, row=1, pady=5)
        Tempxg4.grid(column=3, row=1 )
        
    
    if Tempmvar.get() == True:
        tempmtitg2.grid_forget()
        Tempmg2.grid_forget()

        tempmtitg3.grid_forget()
        Tempmg3.grid_forget()

        tempmtitg4.grid_forget()
        Tempmg4.grid_forget()
    else:
        tempmtitg2.grid(column=2, row=2, pady=5)
        Tempmg2.grid(column=3, row=2 )

        tempmtitg3.grid(column=2, row=2, pady=5)
        Tempmg3.grid(column=3, row=2 )

        tempmtitg4.grid(column=2, row=2, pady=5)
        Tempmg4.grid(column=3, row=2 )
    
    if estvar.get() == True:
        esttitg2.grid_forget()
        esttxtg2.grid_forget()
        estformg2.grid_forget()
        formtitg2.grid_forget()
        formentg2.grid_forget()
        txtentg2.grid_forget()
        txttitg2.grid_forget()

        esttitg3.grid_forget()
        esttxtg3.grid_forget()
        estformg3.grid_forget()
        formtitg3.grid_forget()
        formentg3.grid_forget()
        txtentg3.grid_forget()
        txttitg3.grid_forget()

        esttitg4.grid_forget()
        esttxtg4.grid_forget()
        estformg4.grid_forget()
        formtitg4.grid_forget()
        formentg4.grid_forget()
        txtentg4.grid_forget()
        txttitg4.grid_forget()
    else:
        esttitg2.grid(column=4, row=0, padx=5)
        esttxtg2.grid(column=4, row=1,padx=5)
        estformg2.grid(column=4, row=2,padx=5)

        esttitg3.grid(column=4, row=0, padx=5)
        esttxtg3.grid(column=4, row=1,padx=5)
        estformg3.grid(column=4, row=2,padx=5)

        esttitg4.grid(column=4, row=0, padx=5)
        esttxtg4.grid(column=4, row=1,padx=5)
        estformg4.grid(column=4, row=2,padx=5)

    if matvar.get() == True:
        matnameg2.grid_forget()
        matg2.grid_forget()

        matnameg3.grid_forget()
        matg3.grid_forget()

        matnameg4.grid_forget()
        matg4.grid_forget()
    else:
        matnameg2.grid(column=0, row=0)
        matg2.grid(column=0, row=1)

        matnameg3.grid(column=0, row=0)
        matg3.grid(column=0, row=1)

        matnameg4.grid(column=0, row=0)
        matg4.grid(column=0, row=1)
    
    if fluvar.get() == True:
        flunameg2.grid_forget()
        flug2.grid_forget()

        flunameg3.grid_forget()
        flug3.grid_forget()

        flunameg4.grid_forget()
        flug4.grid_forget()
    else:
        flunameg2.grid(column=1, row=0)
        flug2.grid(column=1, row=1, padx=10)

        flunameg3.grid(column=1, row=0)
        flug3.grid(column=1, row=1, padx=10)

        flunameg4.grid(column=1, row=0)
        flug4.grid(column=1, row=1, padx=10)

def updateg1():
    x1=estg1.get()
    if x1 == 1:
        formtitg1.grid_forget()
        formentg1.grid_forget()
        txtentg1.grid(column=5,row=1,padx=5)
        txttitg1.grid(column=5, row=0)
    if x1 == 2:
        txtentg1.grid_forget()
        txttitg1.grid_forget()
        formtitg1.grid(column=5,row=0)
        formentg1.grid(column=5,row=1,padx=5)

def updateg2():
    x2=estg2.get()
    if x2 == 1:
        formtitg2.grid_forget()
        formentg2.grid_forget()
        txtentg2.grid(column=5,row=1,padx=5)
        txttitg2.grid(column=5, row=0)
    if x2 == 2:
        txtentg2.grid_forget()
        txttitg2.grid_forget()
        formtitg2.grid(column=5,row=0)
        formentg2.grid(column=5,row=1,padx=5)

def updateg3():
    x3=estg3.get()
    if x3 == 1:
        formtitg3.grid_forget()
        formentg3.grid_forget()
        txtentg3.grid(column=5,row=1,padx=5)
        txttitg3.grid(column=5, row=0)
    if x3 == 2:
        txtentg3.grid_forget()
        txttitg3.grid_forget()
        formtitg3.grid(column=5,row=0)
        formentg3.grid(column=5,row=1,padx=5)

def updateg4():
    x4=estg4.get()
    if x4 == 1:
        formtitg4.grid_forget()
        formentg4.grid_forget()
        txtentg4.grid(column=5,row=1,padx=5)
        txttitg4.grid(column=5, row=0)
    if x4 == 2:
        txtentg4.grid_forget()
        txttitg4.grid_forget()
        formtitg4.grid(column=5,row=0)
        formentg4.grid(column=5,row=1,padx=5)

#defs Menu
def openProjeto():
    Projetowin = Toplevel(root)
    Projetowin.title("Sobre o projeto")
    projframe = ttk.Frame(Projetowin, padding=(5, 5, 10, 10))
    projframe.grid(column=0, row=0, sticky=(N,W,E,S))
    Projetowin.grid_columnconfigure(0, weight=1)
    Projetowin.grid_rowconfigure(0,weight=1)

    projtxt=ttk.Label(projframe, text ='Os códigos em Python destacados neste manual têm como finalidade simular o resfriamento de chapas\n'
                                       'metálicas por convecção. Eles foram criados para que o usuário, que fará contato com o programa por meio\n'
                                       'de uma interface gráfica, analise o resfriamento de chapas de diferentes materiais. Vale ressaltar que, para\n'
                                       'facilitar o desenvolvimento do programa, foi definida uma chapa ideal com apenas a face frontal em contato\n'
                                       'com fluidos e objetos de transferência de calor. O programa utiliza o método das diferenças finitas e\n'
                                       'apresenta condições periódicas de contorno da chapa. ')
    projtxt.grid(column=0,row=0)
    Projetowin.mainloop()

def openIntegrantes():
    Integranteswin = Toplevel(root)
    Integranteswin.title("Sobre os Desenvolvedores")
    inteframe = ttk.Frame(Integranteswin, padding=(5, 5, 10, 10))
    inteframe.grid(column=0, row=0, sticky=(N,W,E,S))
    Integranteswin.grid_columnconfigure(0, weight=1)
    Integranteswin.grid_rowconfigure(0,weight=1)

    projtxt=ttk.Label(inteframe, text ="Devs:\n Enzo Benko \n Gabriela Kaori \n Lucas Rogério \n Matheus Capelin \n Pedro Gabriel \n Rafael Cândido")
    projtxt.grid(column=0,row=0)
    Integranteswin.mainloop()


#interface
root=Tk()
root.title('Simulador de resfriamento de chapas finas')

mainframe = ttk.Frame(root, padding=(5, 5, 10, 10))
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)


root.tk.call('source', 'breeze.tcl')
style=ttk.Style(root)
style.theme_use('Breeze')

#Menu
menubar = Menu(root)
root.config(menu=menubar)

about_menu= Menu(menubar, tearoff=False)
about_menu.add_command(label='Projeto', command=openProjeto)
about_menu.add_command(label='Integrantes', command=openIntegrantes)
menubar.add_cascade(
    label="Sobre",
    menu=about_menu,
    underline=0
)

help_menu = Menu(menubar, tearoff=False)
help_menu.add_command(label='Manual')
menubar.add_cascade(
    label="Ajuda",
    menu=help_menu,
    underline=0
)

#Inicio
frametit=ttk.Frame(mainframe, padding=(5, 5, 10, 10))
frametit.grid(column=0,row=0, sticky=(N, W))
img = Image.open("USP.gif")
img = img.resize((75,90), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(img)
eelicon=ttk.Label(frametit, image=photoImg)
eelicon.grid(column=0,row=0,sticky=(N,W))

titulo = ttk.Label(frametit, text="Simulador de resfriamento de chapas finas:", font=('Oswald',16))
titulo.grid(column=1, row=0, sticky=(W),padx=20)

butao=ttk.Button(mainframe, text="Simular", width=15, command=chama)
butao.grid(column=1 , row=0 , sticky=(E))

framein=ttk.Frame(mainframe, padding=(5, 5, 10, 10))
framein.grid(column=0,row=1, sticky=(W))

frase1 = ttk.Label(framein, text="• Utilizar quais dados iguais para todas as chapas:  ")
frase1.grid(column=0, row=0, sticky=(W))
Tempxvar = BooleanVar(value=False)
checkTempx= ttk.Checkbutton(framein, text='Temperatura de estampagem', variable=Tempxvar, onvalue=True, offvalue=False, command=updatecheck)
checkTempx.grid(column=3, row=0, sticky=(W))
Tempmvar = BooleanVar(value=False)
checkTempm= ttk.Checkbutton(framein, text='Temperatura inicial', variable=Tempmvar, onvalue=True, offvalue=False, command=updatecheck)
checkTempm.grid(column=2, row=0, sticky=(W))
matvar = BooleanVar(value=False)
checkmat= ttk.Checkbutton(framein, text='Material', variable=matvar, onvalue=True, offvalue=False, command=updatecheck)
checkmat.grid(column=1, row=1, sticky=(W))
fluvar = BooleanVar(value=False)
checkflu= ttk.Checkbutton(framein, text='Fluido', variable=fluvar, onvalue=True, offvalue=False, command=updatecheck)
checkflu.grid(column=3, row=1, sticky=(W))
estvar = BooleanVar(value=False)
checkest= ttk.Checkbutton(framein, text='Estampagem', variable=estvar, onvalue=True, offvalue=False, command=updatecheck)
checkest.grid(column=1, row=0, sticky=(W))
Tempavar = BooleanVar(value=False)
checkTempa= ttk.Checkbutton(framein, text='Temperatura do fluido', variable=Tempavar, onvalue=True, offvalue=False, command=updatecheck)
checkTempa.grid(column=2, row=1, sticky=(W))

#Grafico 1

titulog1 = ttk.Label(mainframe, text="Chapa 1:", font=('Oswald',14))
titulog1.grid(column=0, row=3, sticky=(W))
frameg1=ttk.Frame(mainframe, padding=(5, 5, 10, 10))
frameg1.grid(column=0, row=4)

matnameg1= ttk.Label(frameg1, text="• Material")
matnameg1.grid(column=0, row=0)
matg1var= StringVar()
matg1= ttk.Combobox(frameg1, textvariable=matg1var)
matg1['values']=('Cobre','Ferro','Alumínio','Bronze','Ouro','Prata','Aço','Chumbo')
matg1.grid(column=0, row=1)

flunameg1= ttk.Label(frameg1, text="• Fluido")
flunameg1.grid(column=1, row=0)
flug1var= StringVar()
flug1= ttk.Combobox(frameg1, textvariable=flug1var)
flug1['values']=('Ar','Ar em movimento','Água','Água em movimento','Óleo','Óleo em movimento')
flug1.grid(column=1, row=1, padx=10)

tempatitg1=ttk.Label(frameg1, text="• Temperatura do fluido:")
tempatitg1.grid(column=2, row=0, pady=5)
Tempambg1= StringVar()
Tempag1=ttk.Entry(frameg1, width=7, textvariable=Tempambg1)
Tempag1.grid(column=3, row=0 )

tempxtitg1=ttk.Label(frameg1, text="• Temperatura de estampagem:")
tempxtitg1.grid(column=2, row=1, pady=5)
Tempmaxg1= StringVar()
Tempxg1=ttk.Entry(frameg1, width=7, textvariable=Tempmaxg1)
Tempxg1.grid(column=3, row=1 )

tempmtitg1=ttk.Label(frameg1, text="• Temperatura inicial:")
tempmtitg1.grid(column=2, row=2, pady=5)
Tempming1= StringVar()
Tempmg1=ttk.Entry(frameg1, width=7, textvariable=Tempming1)
Tempmg1.grid(column=3, row=2 )

estg1=IntVar()
esttitg1=ttk.Label(frameg1, text="• Estampagem:")
esttitg1.grid(column=4, row=0, padx=20, sticky=(W))

esttxtg1=ttk.Radiobutton(frameg1, text="Em texto", variable=estg1, value=1, command=updateg1)
esttxtg1.grid(column=4, row=1,padx=20,sticky=(W))
txtg1=StringVar()
txttitg1=ttk.Label(frameg1, text='• Texto:')
txtentg1=ttk.Entry(frameg1, width=7, textvariable=txtg1)


estformg1=ttk.Radiobutton(frameg1, text="Formas geométricas", variable=estg1, value=2, command=updateg1)
estformg1.grid(column=4, row=2,padx=20, sticky=(W))
formg1=StringVar()
formtitg1=ttk.Label(frameg1, text='• Forma:')
formentg1=ttk.Combobox(frameg1, textvariable=formg1)
formentg1['values']=('Anel circular','Anel elíptico','Círculo','Furo circular')

#Grafico 2 

titulog2 = ttk.Label(mainframe, text="Chapa 2:", font=('Oswald',14))
titulog2.grid(column=0, row=5, sticky=(W))
frameg2=ttk.Frame(mainframe, padding=(5, 5, 10, 10))
frameg2.grid(column=0, row=6)

matnameg2= ttk.Label(frameg2, text="• Material")
matnameg2.grid(column=0, row=0)
matg2var= StringVar()
matg2= ttk.Combobox(frameg2, textvariable=matg2var)
matg2['values']=('Cobre','Ferro','Alumínio','Bronze','Ouro','Prata','Aço','Chumbo')
matg2.grid(column=0, row=1)

flunameg2= ttk.Label(frameg2, text="• Fluido")
flunameg2.grid(column=1, row=0)
flug2var= StringVar()
flug2= ttk.Combobox(frameg2, textvariable=flug2var)
flug2['values']=('Ar','Ar em movimento','Água','Água em movimento','Óleo','Óleo em movimento')
flug2.grid(column=1, row=1, padx=10)

tempatitg2=ttk.Label(frameg2, text="• Temperatura do fluido:")
tempatitg2.grid(column=2, row=0, pady=5)
Tempambg2= StringVar()
Tempag2=ttk.Entry(frameg2, width=7, textvariable=Tempambg2)
Tempag2.grid(column=3, row=0 )

tempxtitg2=ttk.Label(frameg2, text="• Temperatura de estampagem:")
tempxtitg2.grid(column=2, row=1, pady=5)
Tempmaxg2= StringVar()
Tempxg2=ttk.Entry(frameg2, width=7, textvariable=Tempmaxg2)
Tempxg2.grid(column=3, row=1 )

tempmtitg2=ttk.Label(frameg2, text="• Temperatura inicial:")
tempmtitg2.grid(column=2, row=2, pady=5)
Tempming2= StringVar()
Tempmg2=ttk.Entry(frameg2, width=7, textvariable=Tempming2)
Tempmg2.grid(column=3, row=2 )

estg2=IntVar()
esttitg2=ttk.Label(frameg2, text="• Estampagem:")
esttitg2.grid(column=4, row=0, padx=20, sticky=(W))

esttxtg2=ttk.Radiobutton(frameg2, text="Em texto", variable=estg2, value=1, command=updateg2)
esttxtg2.grid(column=4, row=1,padx=20,sticky=(W))
txtg2=StringVar()
txttitg2=ttk.Label(frameg2, text='• Texto:')
txtentg2=ttk.Entry(frameg2, width=7, textvariable=txtg2)


estformg2=ttk.Radiobutton(frameg2, text="Formas geométricas", variable=estg2, value=2, command=updateg2)
estformg2.grid(column=4, row=2,padx=20, sticky=(W))
formg2=StringVar()
formtitg2=ttk.Label(frameg2, text='• Forma:')
formentg2=ttk.Combobox(frameg2, textvariable=formg2)
formentg2['values']=('Anel circular','Anel elíptico','Círculo','Furo circular')

#Grafico 3

titulog3 = ttk.Label(mainframe, text="Chapa 3:", font=('Oswald',14))
titulog3.grid(column=0, row=7, sticky=(W))
frameg3=ttk.Frame(mainframe, padding=(5, 5, 10, 10))
frameg3.grid(column=0, row=8)

matnameg3= ttk.Label(frameg3, text="• Material")
matnameg3.grid(column=0, row=0)
matg3var= StringVar()
matg3= ttk.Combobox(frameg3, textvariable=matg3var)
matg3['values']=('Cobre','Ferro','Alumínio','Bronze','Ouro','Prata','Aço','Chumbo')
matg3.grid(column=0, row=1)

flunameg3= ttk.Label(frameg3, text="• Fluido")
flunameg3.grid(column=1, row=0)
flug3var= StringVar()
flug3= ttk.Combobox(frameg3, textvariable=flug3var)
flug3['values']=('Ar','Ar em movimento','Água','Água em movimento','Óleo','Óleo em movimento')
flug3.grid(column=1, row=1, padx=10)

tempatitg3=ttk.Label(frameg3, text="• Temperatura do fluido:")
tempatitg3.grid(column=2, row=0, pady=5)
Tempambg3= StringVar()
Tempag3=ttk.Entry(frameg3, width=7, textvariable=Tempambg3)
Tempag3.grid(column=3, row=0 )

tempxtitg3=ttk.Label(frameg3, text="• Temperatura de estampagem:")
tempxtitg3.grid(column=2, row=1, pady=5)
Tempmaxg3= StringVar()
Tempxg3=ttk.Entry(frameg3, width=7, textvariable=Tempmaxg3)
Tempxg3.grid(column=3, row=1 )

tempmtitg3=ttk.Label(frameg3, text="• Temperatura inicial:")
tempmtitg3.grid(column=2, row=2, pady=5)
Tempming3= StringVar()
Tempmg3=ttk.Entry(frameg3, width=7, textvariable=Tempming3)
Tempmg3.grid(column=3, row=2 )

estg3=IntVar()
esttitg3=ttk.Label(frameg3, text="• Estampagem:")
esttitg3.grid(column=4, row=0, padx=20, sticky=(W))

esttxtg3=ttk.Radiobutton(frameg3, text="Em texto", variable=estg3, value=1, command=updateg3)
esttxtg3.grid(column=4, row=1,padx=20,sticky=(W))
txtg3=StringVar()
txttitg3=ttk.Label(frameg3, text='• Texto:')
txtentg3=ttk.Entry(frameg3, width=7, textvariable=txtg3)


estformg3=ttk.Radiobutton(frameg3, text="Formas geométricas", variable=estg3, value=2, command=updateg3)
estformg3.grid(column=4, row=2,padx=20, sticky=(W))
formg3=StringVar()
formtitg3=ttk.Label(frameg3, text='• Forma:')
formentg3=ttk.Combobox(frameg3, textvariable=formg3)
formentg3['values']=('Anel circular','Anel elíptico','Círculo','Furo circular')

#Grafico 4

titulog4 = ttk.Label(mainframe, text="Chapa 4:", font=('Oswald',14))
titulog4.grid(column=0, row=9, sticky=(W))
frameg4=ttk.Frame(mainframe, padding=(5, 5, 10, 10))
frameg4.grid(column=0, row=10)

matnameg4= ttk.Label(frameg4, text="• Material")
matnameg4.grid(column=0, row=0)
matg4var= StringVar()
matg4= ttk.Combobox(frameg4, textvariable=matg4var)
matg4['values']=('Cobre','Ferro','Alumínio','Bronze','Ouro','Prata','Aço','Chumbo')
matg4.grid(column=0, row=1)

flunameg4= ttk.Label(frameg4, text="• Fluido")
flunameg4.grid(column=1, row=0)
flug4var= StringVar()
flug4= ttk.Combobox(frameg4, textvariable=flug4var)
flug4['values']=('Ar','Ar em movimento','Água','Água em movimento','Óleo','Óleo em movimento')
flug4.grid(column=1, row=1, padx=10)

tempatitg4=ttk.Label(frameg4, text="• Temperatura do fluido:")
tempatitg4.grid(column=2, row=0, pady=5)
Tempambg4= StringVar()
Tempag4=ttk.Entry(frameg4, width=7, textvariable=Tempambg4)
Tempag4.grid(column=3, row=0 )

tempxtitg4=ttk.Label(frameg4, text="• Temperatura de estampagem:")
tempxtitg4.grid(column=2, row=1, pady=5)
Tempmaxg4= StringVar()
Tempxg4=ttk.Entry(frameg4, width=7, textvariable=Tempmaxg4)
Tempxg4.grid(column=3, row=1 )

tempmtitg4=ttk.Label(frameg4, text="• Temperatura inicial:")
tempmtitg4.grid(column=2, row=2, pady=5)
Tempming4= StringVar()
Tempmg4=ttk.Entry(frameg4, width=7, textvariable=Tempming4)
Tempmg4.grid(column=3, row=2 )

estg4=IntVar()
esttitg4=ttk.Label(frameg4, text="• Estampagem:")
esttitg4.grid(column=4, row=0, padx=20, sticky=(W))

esttxtg4=ttk.Radiobutton(frameg4, text="Em texto", variable=estg4, value=1, command=updateg4)
esttxtg4.grid(column=4, row=1,padx=20,sticky=(W))
txtg4=StringVar()
txttitg4=ttk.Label(frameg4, text='• Texto:')
txtentg4=ttk.Entry(frameg4, width=7, textvariable=txtg4)


estformg4=ttk.Radiobutton(frameg4, text="Formas geométricas", variable=estg4, value=2, command=updateg4)
estformg4.grid(column=4, row=2,padx=20, sticky=(W))
formg4=StringVar()
formtitg4=ttk.Label(frameg4, text='• Forma:')
formentg4=ttk.Combobox(frameg4, textvariable=formg4)
formentg4['values']=('Anel circular','Anel elíptico','Círculo','Furo circular')

root.mainloop()
