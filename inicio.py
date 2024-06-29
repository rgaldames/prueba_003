import csv
import random
from funciones import menu


def ingreso():
    """
    1. Registrar producto:
•	El sistema debe permitir registrar un producto ingresando los siguientes 
    datos: Nombre, Categoría, Cantidad, y Precio (precio aleatorio entre 10 y 1000 generados utilizando random).
•	Validar que todos los datos sean ingresados correctamente (validaciones numéricas y excepciones).
    """
    op='s'
    while op=='s':
        Nombre=input("Nombre Material: ")
        Categoria=input("Categoria: ")
        Cantidad=int(input("Cantidad: "))
        Precio=random.randint(10,1000)
        with open('Materiales.csv','a', newline='') as material:
            escrito=csv.writer(material)
            escrito.writerow(['Nombre','Categoria','Cantidad','Precio'])
            escrito.writerow([Nombre,Categoria,Cantidad,Precio])
        op=input("Desea Ingresar otro (s/n): ")
    material.close

def listar():
    """2. Listar todos los productos:
•	Debe mostrar en la pantalla la lista de todos los productos registrados en el sistema, con el formato similar al siguiente:
    """
    with open('Materiales.csv','r', newline='') as material:
        escrito=csv.reader(material)
        for Row in escrito:
            print("{Nombre} , {Categoria} , {Cantidad} , {Precio}")
            
    
def main():
    while True:
        
        op=menu()
        if op=="1":
            print("----")
            ingreso()
        elif op=="2":
            listar()
        elif op=="3":
            print("listar")
        elif op=="4":
            print("listar")
        elif op=="4":
            break
        
    
if __name__=="__main__":
    main()
