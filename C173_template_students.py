from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random

root = Tk()
root.geometry("900x500")

label_selected_doctor=Label(root)
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)
label_selected_IT=Label(root)
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)
label_selected_chemical=Label(root)
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)

class parent():
    def __init__(self):
        print("Esta es la clase padre")
        
    def doctor(doctor_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = "A "+doctor_name+" se le asignó "+hospital_list[random_hospital]
        
    def softwareEngineer(it_professional_name):
        IT_company_list = ["I code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3) 
        
        #actualiza el siguiente código al guardarlo dentro de la propiedad 'text' de label_selected_IT
        label_selected_IT['text'] = "A "+it_professional_name+" se le asignó "+IT_company_list[random_IT_company]
        
        #define la funcion chemicalEngineer() y dentro de esta pasa la variable chemical_engineer_name
    def chemicalEngineer(chemical_engineer_name):
        #define la variable company_list y dentro de esta guarda la lista de compañías de tu elección en corchetes.
        company_list = ["apollo", "soborte" , "ayuda"]
        # genera un número aleatorio entre 0 y 3 usando la función randint() y guardándolo en la variable random_company
        random_company = random.randint(0,3)
        label_selected_chemical['text'] = "A "+chemical_engineer_name+" se le asignó "+company_list[random_company] 
        
class child1(parent):
    
    def __init__(self):
        print("Esta es la clase child1")
        
    def getDoctor(self):
        name = "Miguel"
        parent.doctor(name)
        
class child2(parent):
    
    def __init__(self):
        print("Esta es la clase child2")
        
    def getIT(self):
        name = "Jessica"
        parent.softwareEngineer(name) 

#define dentro la clase child3(parent).
class child3(parent):
    #define la función the __init__(self) y dentro de esta imprime la declaración como "Esta es la clase child3".
    def the__init__(self):
        print("Esta es la clase child3")
    #define la función getChemical(self) 
    def getChemical(self):
        #define el nombre de la variable y guarda el nombre de tu elección.
        name = "Azariel"
        parent.chemicalEngineer(name)
        
obj1 = child1()
obj2 = child2()
obj3 = child3()
btn_doctor = Button(root, text="Mostrar el hospital asignado", command=obj1.getDoctor)
btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)

btn_it = Button(root, text="Mostrar la compañía TI asignada", command=obj2.getIT)
btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)

btn_chemical = Button(root, text="Mostrar la compañía química asignada", command=obj3.getChemical)
btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)

root.mainloop()