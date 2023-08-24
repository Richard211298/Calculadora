from cgitb import text
from cmath import sqrt
from enum import auto
from tkinter import *
from tkinter import ttk
from tkinter import Tk,Text,Button,END,re
from tkinter import messagebox
import tkinter
import math

#Felix Romero Ricardo
#NOTA:La tasa de interes Simple y Compuesta por el momento solo resuelven sencillas,falta agregar funcion  periodos y ajuste
#Quitar codigo repetitivo
#Agregar ecuacion de valor
#Agregar Tasas equivalente
#Agregar conversor de tasas 

class Aplicacion():
    ''' Clase Aplicacion '''
    
    # Declara una variable de clase para contar ventanas
    
    ventana = 0

    # Declara una variable de clase para usar en el
    # cálculo de la posición de una ventana
    #Felix Romero Ricardo
    
    posx_y = 0
        
    def __init__(self):
        ''' Construye ventana de aplicación '''           
        # Declara ventana de aplicación
        self.raiz = Tk()
        # Define dimensión de la ventana 300x200
        # que se situará en la coordenada x=500,y=50 
        self.raiz.geometry('270x250+900+170')
        ##agregrar imagen de la aplicacion
        #self.raiz.tk.call('wm', 'iconphoto', self.raiz._w, PhotoImage(file='finanzas-icono-png.png'))
        #redondear ventana
        #fondo de la aplicacion

        self.raiz.configure(background='Snow')

        #self.raiz.Tk.call('wm', 'iconphoto', self.raiz._w, Tk.PhotoImage(file='/finanzas-icono-png.png'))
      
        self.raiz.resizable(0,0)
        self.raiz.title("¿Que Solucionar?")# título, mensaje
        Bine=ttk.Label(self.raiz,text="Seleccionar el problema a resolver",background='Snow')
        Bine.place(x=50,y=10)

        #redonderar boton
        #boton1= ttk.Button(self.raiz, text='Precio de Venta',
        #                   command=self.PV,cursor='hand2')
        #boton1.pack(side=BOTTOM, padx=20, pady=20)
        #boton1.place(x=20,y=130)
        #boton1.configure(background='Snow')
        #boton1.configure(foreground='black')
        #boton1.configure(font=('Arial', 10, 'bold'))
        #boton1.configure(width=20)
        #boton1.configure(height=2)
        #boton1.configure(relief='raised')
        #boton1.configure(borderwidth='2')


        boton1 = ttk.Button(self.raiz, text='Precio de Venta', 
                           command=self.PV,cursor='hand2')
        boton1.pack(side=BOTTOM, padx=5, pady=10)

        boton2= ttk.Button(self.raiz, text='Cantidad a producir', 
                           command=self.CP,cursor='hand2')
        boton2.pack(side=BOTTOM, padx=5, pady=10)

        boton3= ttk.Button(self.raiz, text='Maximisacion ingresos', 
                           command=self.MAI,cursor='hand2')
        boton3.pack(side=BOTTOM, padx=5, pady=10)

        boton4= ttk.Button(self.raiz, text='Tasas', 
                           command=self.CAP,cursor='hand2')
        boton4.pack(side=BOTTOM, padx=5, pady=10)


        boton1.place(x=50,y=50)
        boton2.place(x=50,y=90)
        boton3.place(x=50,y=130)
        boton4.place(x=50,y=170)



        self.raiz.mainloop()

    def PV (self):
        
        
        # Define una nueva ventana de diálogo
        
        self.dialogo = Toplevel()
        
        # Incrementa en 1 el contador de ventanas
        
        Aplicacion.ventana+=1
        #self.dialogo.tk.call('wm', 'iconphoto', self.dialogo._w, PhotoImage(file='finanzas-icono-png.png'))        
        # Recalcula posición de la ventana
        #fondo snow
        self.dialogo.configure(background='Snow')

        
        Aplicacion.posx_y += 50
        self.dialogo.geometry('255x200+400+200')
        self.dialogo.title("Precio de Venta")# título, mensaje
        self.dialogo.resizable(0,0)

        text1=ttk.Label(self.dialogo,text="Costo por Unidad",background='Snow')
        text1.place(x=15,y=30)
        sd=ttk.Label(self.dialogo,text="$",background='Snow')
        sd.place(x=120,y=30)
        self.dato1=tkinter.DoubleVar()
        entry1=ttk.Entry(self.dialogo,width=10,textvariable=self.dato1)
        entry1.place(x=130,y=30)

        text2=ttk.Label(self.dialogo,text="Utilidad Deseada",background='Snow')
        text2.place(x=15,y=60)
        sp=ttk.Label(self.dialogo,text="%",background='Snow')
        sp.place(x=200,y=60)
        self.dato2=tkinter.DoubleVar()
        entry2=ttk.Entry(self.dialogo,width=10,textvariable=self.dato2)
        entry2.place(x=130,y=60)


        text3=ttk.Label(self.dialogo,text="Descuento",background='Snow')
        text3.place(x=15,y=90)
        sp1=ttk.Label(self.dialogo,text="%",background='Snow')
        sp1.place(x=200,y=90)
        self.dato3=tkinter.DoubleVar()
        entry3=ttk.Entry(self.dialogo,width=10,textvariable=self.dato3)
        entry3.place(x=130,y=90)

        boton5= ttk.Button(self.dialogo, text='Cerrar', 
                           command=self.dialogo.destroy,cursor='hand2')   
        boton5.pack(side=BOTTOM, padx=20, pady=20)
        boton6= ttk.Button(self.dialogo, text='Dar precio', 
                           command=self.Dar,cursor='hand2')
        boton6.pack(side=BOTTOM, padx=20, pady=20)


        boton5.place(x=130,y=170)

        boton6.place(x=20,y=130)

        self.raiz.wait_window(self.dialogo)

    def Dar (self):
        dato1=(self.dato1.get())
        dato2=(self.dato2.get())
        dato3=(self.dato3.get())

        if dato3==0:
            Resultado=(dato1*(dato2/100))+dato1
            #redondear a dos decimales
            Resultado=round(Resultado,2)
            #Limitar salida a dos decimales
            Resultado=str(Resultado)
            Resultado=Resultado[0:2]
            #mensaje de resultado
            res=ttk.Label(self.dialogo,text="Precio de venta: $"+Resultado)
            res.place(x=100,y=130)
        
        else :
            Resultado=(dato1*(dato2/100))+dato1
            Resultado=(Resultado*(dato3/100))+Resultado
            Resultado=str(Resultado)
            res=ttk.Label(self.dialogo,text="Precio de venta: $"+Resultado)
            res.place(x=100,y=130)
        
    def CP(self):
        
        self.dialogo = Toplevel()
        
        # Incrementa en 1 el contador de ventanas#Felix Romero Ricardo
        
        Aplicacion.ventana+=1
        
        # Recalcula posición de la ventana
        
        Aplicacion.posx_y += 50
        self.dialogo.geometry('250x240+400+200')
        self.dialogo.title("Cantidad a Producir")# título, mensaje
        self.dialogo.resizable(0,0)
        #self.dialogo.tk.call('wm', 'iconphoto', self.dialogo._w, PhotoImage(file='finanzas-icono-png.png'))  
        #fondo snow
        self.dialogo.configure(background='Snow')


        text1=ttk.Label(self.dialogo,text="Costo Fijo",background='Snow')
        text1.place(x=15,y=30)
        sd=ttk.Label(self.dialogo,text="$",background='Snow')
        sd.place(x=120,y=30)
        self.dato1=tkinter.DoubleVar()
        entry1=ttk.Entry(self.dialogo,width=10,textvariable=self.dato1)
        entry1.place(x=130,y=30)

        text2=ttk.Label(self.dialogo,text="Costo Variable",background='Snow')
        text2.place(x=15,y=60)
        sp=ttk.Label(self.dialogo,text="$",background='Snow')
        sp.place(x=120,y=60)
        self.dato2=tkinter.DoubleVar()
        entry2=ttk.Entry(self.dialogo,width=10,textvariable=self.dato2)
        entry2.place(x=130,y=60)


        text3=ttk.Label(self.dialogo,text="Precio de venta",background='Snow')
        text3.place(x=15,y=90)
        sp1=ttk.Label(self.dialogo,text="$",background='Snow')
        sp1.place(x=120,y=90)
        self.dato3=tkinter.DoubleVar()
        entry3=ttk.Entry(self.dialogo,width=10,textvariable=self.dato3)
        entry3.place(x=130,y=90)

        text4=ttk.Label(self.dialogo,text="Utilidad igual a",background='Snow')
        text4.place(x=15,y=120)
        sp3=ttk.Label(self.dialogo,text="$",background='Snow')
        sp3.place(x=120,y=120)
        self.dato4=tkinter.DoubleVar()
        entry4=ttk.Entry(self.dialogo,width=10,textvariable=self.dato4)
        entry4.place(x=130,y=120)
              
        
        
        boton5= ttk.Button(self.dialogo, text='Cerrar', 
                           command=self.dialogo.destroy,cursor='hand2')
        boton5.pack(side=BOTTOM, padx=20, pady=20)

        boton6= ttk.Button(self.dialogo, text='Dar produccion', 
                           command=self.Dp,cursor='hand2')
        boton6.pack(side=BOTTOM, padx=20, pady=20)


        boton5.place(x=130,y=200)

        boton6.place(x=5,y=160)

        self.raiz.wait_window(self.dialogo)

    def Dp (self):

        dato1=(self.dato1.get())
        dato2=(self.dato2.get())
        dato3=(self.dato3.get())
        dato4=(self.dato4.get())

        Resultado=(dato4+dato1)/(dato3-dato2)
        Resultado=round(Resultado,2)

        #redondear a dos decimales
        Resultado=str(Resultado)
  

        res=ttk.Label(self.dialogo,text="Produccion: "+Resultado,background='Snow')
        res.place(x=100,y=160)
    
    def MAI(self):    
        
        self.dialogo = Toplevel()
        
        # Incrementa en 1 el contador de ventanas
        
        Aplicacion.ventana+=1
        
        # Recalcula posición de la ventana
        
        Aplicacion.posx_y += 50
        self.dialogo.geometry('255x280+400+200')
        self.dialogo.title("Maximisacion")# título, mensaje
        self.dialogo.resizable(0,0)
        #self.dialogo.tk.call('wm', 'iconphoto', self.dialogo._w, PhotoImage(file='finanzas-icono-png.png')) 
        #fondo snow
        self.dialogo.configure(background='Snow')

         
        text1=ttk.Label(self.dialogo,text="Depa,Casas,Unid.",background='Snow')
        text1.place(x=15,y=30)
        sd=ttk.Label(self.dialogo,text="#",background='Snow')
        sd.place(x=200,y=30)
        self.dato1=tkinter.DoubleVar()
        entry1=ttk.Entry(self.dialogo,width=10,textvariable=self.dato1)
        entry1.place(x=130,y=30)

        text2=ttk.Label(self.dialogo,text="Si sube valor",background='Snow')
        text2.place(x=15,y=60)
        sp=ttk.Label(self.dialogo,text="$",background='Snow')
        sp.place(x=120,y=60)
        self.dato2=tkinter.DoubleVar()
        entry2=ttk.Entry(self.dialogo,width=10,textvariable=self.dato2)
        entry2.place(x=130,y=60)


        text3=ttk.Label(self.dialogo,text="Baja D,C,U.",background='Snow')
        text3.place(x=15,y=90)
        sp1=ttk.Label(self.dialogo,text="#",background='Snow')
        sp1.place(x=200,y=90)
        self.dato3=tkinter.DoubleVar()
        entry3=ttk.Entry(self.dialogo,width=10,textvariable=self.dato3)
        entry3.place(x=130,y=90)

        text4=ttk.Label(self.dialogo,text="Ingresos deseados",background='Snow')
        text4.place(x=15,y=120)
        sp2=ttk.Label(self.dialogo,text="$",background='Snow')
        sp2.place(x=120,y=120)
        self.dato4=tkinter.DoubleVar()
        entry4=ttk.Entry(self.dialogo,width=10,textvariable=self.dato4)
        entry4.place(x=130,y=120)

        text5=ttk.Label(self.dialogo,text="Precio minimo",background='Snow')
        text5.place(x=15,y=150)
        sp3=ttk.Label(self.dialogo,text="$",background='Snow')
        sp3.place(x=120,y=150)
        self.dato5=tkinter.DoubleVar()
        entry5=ttk.Entry(self.dialogo,width=10,textvariable=self.dato5)
        entry5.place(x=130,y=150)
   
        boton5= ttk.Button(self.dialogo, text='Cerrar', 
                           command=self.dialogo.destroy,cursor='hand2')
        boton5.pack(side=BOTTOM, padx=20, pady=20)

        boton6= ttk.Button(self.dialogo, text='Dar precio', 
                           command=self.Dap,cursor='hand2')
        boton6.pack(side=BOTTOM, padx=20, pady=20)


        boton5.place(x=130,y=230)

        boton6.place(x=20,y=190)

        self.raiz.wait_window(self.dialogo)

    def Dap (self):

        dato1=(self.dato1.get())
        dato2=(self.dato2.get())
        a=(self.dato3.get())
        c=(self.dato4.get())*(dato2)
        dato5=(self.dato5.get())
        b=(((dato5*a)+(dato1*dato2))*-1)
        x=(b*b)-(4*a*c)

        if x <=0 :
            res=ttk.Label(self.dialogo,text="No se puede",background='Snow')
            res.place(x=110,y=190)
            
        else :
            Res1=(((b*-1)+sqrt(x)))/(2*a)

            Res2=(((b*-1)-sqrt(x)))/(2*a)



            Res1=str(Res1)
   
            Res2=str(Res2)
  
            

            res=ttk.Label(self.dialogo,text="Valor 1: $"+ Res1,background='Snow')
            res.place(x=110,y=180)
            resc=ttk.Label(self.dialogo,text="Valor 2: $"+Res2,background='Snow')
            resc.place(x=110,y=200)

    def CAP(self):    
        
        self.dialogo = Toplevel()
        # Incrementa en 1 el contador de ventanas
        Aplicacion.ventana+=1
        # Recalcula posición de la ventana
        Aplicacion.posx_y += 50
        self.dialogo.geometry('200x200+600+200')
        self.dialogo.title("Tasas")# título, mensaje
        self.dialogo.resizable(0,0)
        #self.dialogo.tk.call('wm', 'iconphoto', self.dialogo._w, PhotoImage(file='finanzas-icono-png.png'))  
        #fondo snow
        self.dialogo.configure(background='Snow')

        boton5= ttk.Button(self.dialogo, text='Cerrar', 
                           command=self.dialogo.destroy,cursor='hand2')
        boton5.pack(side=BOTTOM, padx=20, pady=20)

        boton6= ttk.Button(self.dialogo, text='Interes Simple', 
                           command=self.INTS,cursor='hand2')
        boton6.pack(side=BOTTOM, padx=20, pady=20)

        boton7= ttk.Button(self.dialogo, text='Interes Compuesto', 
                           command=self.INTC,cursor='hand2')
        boton7.pack(side=BOTTOM, padx=20, pady=20)

        boton8= ttk.Button(self.dialogo, text='Tasa efectiva', 
                           command=self.INTE,cursor='hand2')
        boton8.pack(side=BOTTOM, padx=20, pady=20)

        boton9= ttk.Button(self.dialogo, text='Tasa real', 
                           command=self.TR,cursor='hand2')
        boton9.pack(side=BOTTOM, padx=20, pady=20)


        boton5.place(x=100,y=170)
        boton6.place(x=20,y=20)
        boton7.place(x=20,y=50)
        boton8.place(x=20,y=80)
        boton9.place(x=20,y=110)

        self.raiz.wait_window(self.dialogo)

    def  INTS (self):
        Time=("Dia","Semana","Mes","Año")

        self.panic=Toplevel()

        Aplicacion.ventana+=1

        Aplicacion.posx_y+=50

        self.panic.geometry('300x255+280+200')
        self.panic.resizable(0,0)
        self.panic.title("Interes simple")
        #self.panic.tk.call('wm', 'iconphoto', self.panic._w, PhotoImage(file='finanzas-icono-png.png'))  
        #fondo snow
        self.panic.configure(background='Snow')
        text1=ttk.Label(self.panic,text="Capital Inicial",background='Snow')
        text1.place(x=15,y=30)
        sd=ttk.Label(self.panic,text="$",background='Snow')
        sd.place(x=120,y=30)
        self.dato1=tkinter.DoubleVar()
        entry1=ttk.Entry(self.panic,width=10,textvariable=self.dato1)
        entry1.place(x=130,y=30)

        text2=ttk.Label(self.panic,text="Ganancia",background='Snow')
        text2.place(x=15,y=60)
        sd1=ttk.Label(self.panic,text="$",background='Snow')
        sd1.place(x=120,y=60)
        self.dato2=tkinter.DoubleVar()
        entry2=ttk.Entry(self.panic,width=10,textvariable=self.dato2)
        entry2.place(x=130,y=60)

        text4=ttk.Label(self.panic,text="Periodos",background='Snow')
        text4.place(x=15,y=90)

###################################
        self.Tiempo1=tkinter.StringVar()
        CT1=ttk.Combobox(self.panic,width=10,textvariable=self.Tiempo1,values=Time)
        CT1.current(0)
        CT1.grid(column=0,row=1)
        CT1.place(x=210,y=90)
#################################

        self.dato4=tkinter.DoubleVar()
        entry4=ttk.Entry(self.panic,width=10,textvariable=self.dato4)
        entry4.place(x=130,y=90)



        text5=ttk.Label(self.panic,text="Tasa",background='Snow')
        text5.place(x=15,y=120)
        sd4=ttk.Label(self.panic,text="%",background='Snow')
        sd4.place(x=195,y=120)

###################################
        self.Tiempo2=tkinter.StringVar()
        CT2=ttk.Combobox(self.panic,width=10,textvariable=self.Tiempo2,values=Time)
        CT2.current(0)
        CT2.grid(column=0,row=1)
        CT2.place(x=210,y=120)
#################################

        self.dato5=tkinter.DoubleVar()
        entry5=ttk.Entry(self.panic,width=10,textvariable=self.dato5)
        entry5.place(x=130,y=120)


        boton10= ttk.Button(self.panic, text='Cerrar', 
                           command=self.panic.destroy,cursor='hand2')
        boton10.pack(side=BOTTOM, padx=20, pady=20)
        boton11= ttk.Button(self.panic, text='Determinar', 
                           command=self.Ders,cursor='hand2')
        boton11.pack(side=BOTTOM, padx=20, pady=20)   

        boton10.place(x=200,y=210)   
        boton11.place(x=15,y=180)  

    def Ders (self) :

        dato1=(self.dato1.get())
        dato2=(self.dato2.get())  
        dato3=(self.dato4.get())
        dato4=(self.dato5.get())
        TIME2=self.Tiempo1.get()
        TIME3=self.Tiempo2.get()

        if dato4 !=0:
            if TIME2=="Dia":
                if TIME3=="Dia":
                 dato=dato4/100
                elif TIME3== "Semana":
                  dato=(dato4/7)/100
                elif TIME3 == "Mes":
                 dato=(dato4/30)/100
                elif TIME3 == "Año":
                 dato=(dato4/360)/100
            
            elif TIME2== "Semana":
                if TIME3=="Dia":
                 dato=(dato4*7)/100
                elif TIME3== "Semana":
                 dato=(dato4)/100
                elif TIME3 == "Mes":
                 dato=(dato4/4)/100
                elif TIME3 == "Año":
                 dato=(dato4/52)/100

            elif TIME2 == "Mes":
                if TIME3=="Dia":
                  dato=(dato4*30)/100
                elif TIME3== "Semana":
                 dato=(dato4*4)/100
                elif TIME3 == "Mes":
                 dato=(dato4)/100
                elif TIME3 == "Año":
                 dato=(dato4/12)/100
            
            elif TIME2 == "Año":
               if TIME3=="Dia":
                 dato=(dato4*360)/100
               elif TIME3== "Semana":
                  dato=(dato4*52)/100
               elif TIME3 == "Mes":
                 dato=(dato4*12)/100
               elif TIME3 == "Año":
                 dato=(dato4)/100
        

        if dato1 == 0:
            Resultado=dato2/(1+(dato*dato3))
            Resultado=round(Resultado,2)
   
            Resultado=str(Resultado)
      
  
            res=ttk.Label(self.panic,text="Capital INI  "+ Resultado,background='Snow')
            res.place(x=100,y=180)
        elif dato2==0:
            Resultado=dato1*(1+(dato*dato3))
            Resultado=round(Resultado,2)
      
            Resultado=str(Resultado)

            res=ttk.Label(self.panic,text="Capital FIN  "+ Resultado,background='Snow')
            res.place(x=100,y=180)
        elif dato3==0:
            Resultado=((dato2/dato1)-1)/dato
            Resultado=round(Resultado,2)
            Resultado=str(Resultado)
         
   
            res=ttk.Label(self.panic,text="Periodos  "+" "+TIME2 +" "+ Resultado,background='Snow')
            res.place(x=100,y=180)
        elif dato4==0:
            Resultado=((dato2/dato1)-1)/dato3
            Resultado=round(Resultado,4)
            Resultado=str(Resultado)

            res=ttk.Label(self.panic,text="Interes  "+" "+TIME2 +" "+Resultado,background='Snow')
            res.place(x=100,y=180)
   
    def  INTC (self):
        Time=("Dia","Semana","Mes","Año")

        self.panic=Toplevel()

        Aplicacion.ventana+=1

        Aplicacion.posx_y+=50

        self.panic.geometry('300x250+280+200')
        self.panic.resizable(0,0)
        self.panic.title("Interes compuesto")
        #self.panic.tk.call('wm', 'iconphoto', self.panic._w, PhotoImage(file='finanzas-icono-png.png'))
        #fondo snow
        self.panic.configure(background='Snow')
        text1=ttk.Label(self.panic,text="Capital Inicial",background='Snow')
        text1.place(x=15,y=30)
        sd=ttk.Label(self.panic,text="$",background='Snow')
        sd.place(x=120,y=30)
        self.dato1=tkinter.DoubleVar()
        entry1=ttk.Entry(self.panic,width=10,textvariable=self.dato1)
        entry1.place(x=130,y=30)

        text2=ttk.Label(self.panic,text="Ganancia",background='Snow')
        text2.place(x=15,y=60)
        sd1=ttk.Label(self.panic,text="$",background='Snow')
        sd1.place(x=120,y=60)
        self.dato2=tkinter.DoubleVar()
        entry2=ttk.Entry(self.panic,width=10,textvariable=self.dato2)
        entry2.place(x=130,y=60)

        text4=ttk.Label(self.panic,text="Periodos",background='Snow')
        text4.place(x=15,y=90)

###################################
        self.Tiempo1=tkinter.StringVar()
        CT1=ttk.Combobox(self.panic,width=10,textvariable=self.Tiempo1,values=Time)
        CT1.current(0)
        CT1.grid(column=0,row=1)
        CT1.place(x=210,y=90)
#################################

        self.dato4=tkinter.DoubleVar()
        entry4=ttk.Entry(self.panic,width=10,textvariable=self.dato4)
        entry4.place(x=130,y=90)



        text5=ttk.Label(self.panic,text="Tasa",background='Snow')
        text5.place(x=15,y=120)
        sd4=ttk.Label(self.panic,text="%",background='Snow')
        sd4.place(x=195,y=120)

###################################
        self.Tiempo2=tkinter.StringVar()
        CT2=ttk.Combobox(self.panic,width=10,textvariable=self.Tiempo2,values=Time)
        CT2.current(0)
        CT2.grid(column=0,row=1)
        CT2.place(x=210,y=120)
#################################

        self.dato5=tkinter.DoubleVar()
        entry5=ttk.Entry(self.panic,width=10,textvariable=self.dato5)
        entry5.place(x=130,y=120)


        boton10= ttk.Button(self.panic, text='Cerrar', 
                           command=self.panic.destroy,cursor='hand2')
        boton10.pack(side=BOTTOM, padx=20, pady=20)
        boton11= ttk.Button(self.panic, text='Determinar', 
                           command=self.Dert,cursor='hand2')
        boton11.pack(side=BOTTOM, padx=20, pady=20)   

        boton10.place(x=200,y=210)   
        boton11.place(x=15,y=180)  

    def Dert (self) :

        dato1=(self.dato1.get())
        dato2=(self.dato2.get())  
        dato3=(self.dato4.get())
        dato4=(self.dato5.get())
        TIME2=self.Tiempo1.get()
        TIME3=self.Tiempo2.get()

        if dato4 !=0:
            if TIME2=="Dia":
                if TIME3=="Dia":
                 dato=dato4/100
                elif TIME3== "Semana":
                  dato=(dato4/7)/100
                elif TIME3 == "Mes":
                 dato=(dato4/30)/100
                elif TIME3 == "Año":
                 dato=(dato4/360)/100
            
            elif TIME2== "Semana":
                if TIME3=="Dia":
                 dato=(dato4*7)/100
                elif TIME3== "Semana":
                 dato=(dato4)/100
                elif TIME3 == "Mes":
                 dato=(dato4/4)/100
                elif TIME3 == "Año":
                 dato=(dato4/52)/100

            elif TIME2 == "Mes":
                if TIME3=="Dia":
                  dato=(dato4*30)/100
                elif TIME3== "Semana":
                 dato=(dato4*4)/100
                elif TIME3 == "Mes":
                 dato=(dato4)/100
                elif TIME3 == "Año":
                 dato=(dato4/12)/100
            
            elif TIME2 == "Año":
               if TIME3=="Dia":
                 dato=(dato4*360)/100
               elif TIME3== "Semana":
                  dato=(dato4*52)/100
               elif TIME3 == "Mes":
                 dato=(dato4*12)/100
               elif TIME3 == "Año":
                 dato=(dato4)/100
        

        if dato1 == 0:
            Resultado=(1+dato)**dato3
            Resultado=dato2/Resultado
            Resultado=round(Resultado,2)
            Resultado=str(Resultado)
            res=ttk.Label(self.panic,text="Capital INI  "+ Resultado,background='Snow')
            res.place(x=100,y=180)
        elif dato2==0:
            Resultado=(1+dato)**dato3
            Resultado=dato1*Resultado
            Resultado=round(Resultado,2)
            Resultado=str(Resultado)
            res=ttk.Label(self.panic,text="Capital FIN  "+ Resultado,background='Snow')
            res.place(x=100,y=180)
        elif dato3==0:
            AH=math.log(dato2/dato1)
            AB=math.log(1+dato)
            Resultado=AH/AB
            Resultado=round(Resultado,2)
            Resultado=str(Resultado)
            res=ttk.Label(self.panic,text="Periodos  "+" "+TIME2+" "+ Resultado,background='Snow')
            res.place(x=100,y=180)
        elif dato4==0:
            Resultado=(dato2/dato1)**(1/dato3)
            Resultado=Resultado-1
            Resultado=round(Resultado,2)
            Resultado=str(Resultado)
            res=ttk.Label(self.panic,text="Interes  " +" "+TIME2+" "+ Resultado,background='Snow')
            res.place(x=100,y=180)

    def  INTE (self):
    
        self.panic=Toplevel()

        Aplicacion.ventana+=1

        Aplicacion.posx_y+=50

        self.panic.geometry('300x210+280+200')
        self.panic.resizable(0,0)
        self.panic.title("Tasa efectiva")
        #self.panic.tk.call('wm', 'iconphoto', self.panic._w, PhotoImage(file='finanzas-icono-png.png'))
        #fondo snow
        self.panic.configure(background='Snow')
        text3=ttk.Label(self.panic,text="Tasa",background='Snow')
        text3.place(x=15,y=30)
        sd4=ttk.Label(self.panic,text="%",background='Snow')
        sd4.place(x=195,y=30)
###################################
    #Felix Romero Ricardo
#################################
        self.dato3=tkinter.DoubleVar()
        entry3=ttk.Entry(self.panic,width=10,textvariable=self.dato3)
        entry3.place(x=130,y=30)

        text4=ttk.Label(self.panic,text="Periodos",background='Snow')
        text4.place(x=15,y=60)

###################################

#################################

        self.dato4=tkinter.DoubleVar()
        entry4=ttk.Entry(self.panic,width=10,textvariable=self.dato4)
        entry4.place(x=130,y=60)

        boton10= ttk.Button(self.panic, text='Cerrar', 
                           command=self.panic.destroy,cursor='hand2')
        boton10.pack(side=BOTTOM, padx=20, pady=20)
        boton11= ttk.Button(self.panic, text='Determinar', 
                           command=self.TEFEC,cursor='hand2')
        boton11.pack(side=BOTTOM, padx=20, pady=20)   

        boton10.place(x=200,y=180)   
        boton11.place(x=15,y=120) 

    def TEFEC (self):

        dato3=((self.dato3.get())/100)
        dato4=(self.dato4.get())
      
        Resultado=(1+dato3/dato4)**dato4
        Resultado=Resultado-1
        Resultado=round(Resultado,6)
        Resultado=str(Resultado)
        res=ttk.Label(self.panic,text="Tasa efectiva anual "+Resultado,background='Snow')
        res.place(x=100,y=120)
   
    def  TR (self):
        Time=("Dia","Semana","Mes","Año")

        self.panic=Toplevel()

        Aplicacion.ventana+=1

        Aplicacion.posx_y+=50

        self.panic.geometry('300x210+280+200')
        self.panic.resizable(0,0)
        self.panic.title("Tasa Real")

        #self.panic.tk.call('wm', 'iconphoto', self.panic._w, PhotoImage(file='finanzas-icono-png.png'))
        #fondo snow
        self.panic.configure(background='Snow') 

        text3=ttk.Label(self.panic,text="Tasa ",background='Snow')
        text3.place(x=15,y=30)
        sd4=ttk.Label(self.panic,text="%",background='Snow')
        sd4.place(x=195,y=30)
###################################
        self.Tiempo=tkinter.StringVar()
        CT=ttk.Combobox(self.panic,width=10,textvariable=self.Tiempo,values=Time)
        CT.current(0)
        CT.grid(column=0,row=1)
        CT.place(x=210,y=30)
##################################Felix Romero Ricardo
        self.dato3=tkinter.DoubleVar()
        entry3=ttk.Entry(self.panic,width=10,textvariable=self.dato3)
        entry3.place(x=130,y=30)


        text4=ttk.Label(self.panic,text="Tasa de inflacion",background='Snow')
        text4.place(x=15,y=60)
        sd3=ttk.Label(self.panic,text="%",background='Snow')
        sd3.place(x=195,y=60)

###################################
        self.Tiempo1=tkinter.StringVar()
        CT1=ttk.Combobox(self.panic,width=10,textvariable=self.Tiempo1,values=Time)
        CT1.current(0)
        CT1.grid(column=0,row=1)
        CT1.place(x=210,y=60)
#################################

        self.dato4=tkinter.DoubleVar()
        entry4=ttk.Entry(self.panic,width=10,textvariable=self.dato4)
        entry4.place(x=130,y=60)


        boton10= ttk.Button(self.panic, text='Cerrar', 
                           command=self.panic.destroy,cursor='hand2')
        boton10.pack(side=BOTTOM, padx=20, pady=20)
        boton11= ttk.Button(self.panic, text='Determinar', 
                           command=self.INRE,cursor='hand2')
        boton11.pack(side=BOTTOM, padx=20, pady=20)   

        boton10.place(x=200,y=180)   
        boton11.place(x=15,y=120) 

    def INRE (self):

        dato3=(self.dato3.get())
        dato4=(self.dato4.get())
        TN=self.Tiempo.get()
        INF=self.Tiempo1.get()


        if TN=="Dia":
            dato=(dato3*360)/100
        elif TN == "Semana":
            dato=(dato3*52)/100
        elif TN == "Mes":
            dato=(dato3*12)/100
        elif TN == "Año":
            dato=(dato3)/100
        
        if INF=="Dia":
            dato10=(dato4*360)/100
        elif INF == "Semana":
            dato10=(dato4*52)/100
        elif INF == "Mes":
            dato10=(dato4*12)/100
        elif INF == "Año":
            dato10=(dato4)/100
        

        Resultado=((1+dato)/(1+dato10))-1
        Resultado=round(Resultado,4)

        Resultado=str(Resultado)
        res=ttk.Label(self.panic,text="Tasa real anual "+ Resultado,background='Snow')
        res.place(x=100,y=120)



def main():
    mi_app = Aplicacion()
    return(0)

if __name__ == '__main__':
    main()

