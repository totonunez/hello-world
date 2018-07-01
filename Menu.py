from ListaContactos import *
from ArbolContactos import *
from AvlContactos import *
from HashContacto import *

class Menu:
    def __init__(self):
        self.head = None
        self.cont = 0

    def Inicio(self):
        print("Bienvenido a su lista de contactos \nIngrese la lista que desee implementar en sus Contactos")
        print("1. Lista de Contacto")
        print("2. Arbol Binario")
        print("3. AVL")
        print("4. Arbol_2_3")
        print("5. Hashing")
        op=int(input("Ingrese opcion: "))
        if op==1:
            self.Lista()
        elif op==2:
            self.ArbolBinario()
        elif op==3:
            self.AVLtree()
        elif op==4:
            self.Arbolito23()
        elif op==5:
            self.Hashing()
        else:
            print("A ingresado una opción no valida, por favor vuelva a ingresar opcion")
            self.Inicio()

    def Lista(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar N Contactos")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            if self.head == None:
                self.head = ListaContactos()
            n = int(input("Ingrese la Cantidad de contactos que desea tener en su lista: "))
            self.head.agregarNContactos(n)
            self.cont +=n
            self.Lista()

        elif op==2:
            if self.head == None:
                print("No puede eliminar Contactos, dado que no hay ninguno\n")
                self.Lista()
            else:
                self.head.Eliminar()
                self.cont -=1
                self.Lista()

        elif op==3:
            if self.head == None:
                print("No se encuentran Contactos disponible, porfavor ingrese otra opcion")
                self.Lista()
            else:
                self.head.printList()
                self.Lista()

        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.head = None
                self.cont = 0
                self.Inicio()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.Lista()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.Lista()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.Lista()

    def ArbolBinario(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            if self.head == None:
                self.head = ArbolContactos()
            n = int(input("Ingrese la Cantidad de contactos que desea tener en su lista: "))
            self.head.agregarNContactos(n)
            self.cont +=n
            self.ArbolBinario()

        elif op==2:
            if self.head == None:
                print("No puede eliminar Contactos, dado que no hay ninguno\n")
                self.ArbolBinario()
            else:
                self.head.eliminarContacto()
                self.cont -=1
                self.ArbolBinario()

        elif op==3:
            if self.head == None:
                print("No se encuentran Contactos disponible, porfavor ingrese otra opcion")
                self.ArbolBinario()
            else:
                self.head.InOrder(self.head.root)
                self.ArbolBinario()

        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.head = None
                self.Inicio()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.ArbolBinario()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.ArbolBinario()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.ArbolBinario()


    def AVLtree(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            n = int(input("Ingrese la Cantidad de contactos que desea tener en su lista: "))
            if self.head == None:
                self.head = AVLTree()
            self.head.agregarNContactos(n)
            self.cont +=1
            self.AVLtree()

        elif op==2:
            if self.head == None:
                print("No puede eliminar Contactos, dado que no hay ninguno\n")
                self.AVLtree()
            else:
                self.head.eliminarContacto()
                self.cont -=1
                self.AVLtree()

        elif op==3:
            if self.head == None:
                print("No se encuentran Contactos disponible, porfavor ingrese otra opcion")
                self.AVLtree()
            else:
                self.head.display()
                self.AVLtree()

        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.head = None
                self.Inicio()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.AVLtree()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.AVLtree()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.AVLtree()

    def Arbolito23(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            if self.head == None:
                self.head = Arbol23Contactos()
            self.head.agregarContacto()
            self.cont +=1
            self.Arbolito23()

        elif op==2:
            if self.head == None:
                print("No puede eliminar Contactos, dado que no hay ninguno\n")
                self.Arbolito23()
            else:
                self.head.eliminarContacto()
                self.cont -=1
                self.Arbolito23()

        elif op==3:
            if self.head == None:
                print("No se encuentran Contactos disponible, porfavor ingrese otra opcion")
                self.Arbolito23()
            else:
                self.head.printList()
                self.Arbolito23()

        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.head = None
                self.Arbolito23()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.Arbolito23()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.Arbolito23()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.Arbolito23()


    def Hashing(self):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            if self.head == None:
                tam = int(input("Seleccione el tamaño de su lista hash: "))
                self.head = HashContacto(tam)
            n = int(input("Ingrese la Cantidad de contactos que desea tener en su lista: "))
            self.head.agregarNContactos(n)
            self.cont +=1
            self.Hashing()

        elif op==2:
            if self.head == None:
                print("No puede eliminar Contactos, dado que no hay ninguno\n")
                self.Hashing()
            else:
                key = input("Ingresar clave para eliminar contacto")
                self.head.getEliminarHash(key)
                self.cont -=1
                self.Hashing()

        elif op==3:
            if self.head == None:
                print("No se encuentran Contactos disponible, porfavor ingrese otra opcion")
                self.Hashing()
            else:
                self.head.printHash()
                self.Hashing()

        elif op==0:
            print("¿ Esta seguro de eliminar la estructura de datos ?")
            print("1.Si \n2.No")
            aux = int(input("Ingrese opcion: "))
            if aux == 1:
                self.head = None
                self.Inicio()

            elif aux==2:
                print("Reiniciar Menu de Lista\n")
                self.Hashing()
            else:
                print("Opcion no valida, por favor ingrese valores correctos")
                self.Hashing()

        else:
            print("Opcion no valida, por favor ingresar opción valida.")
            self.Hashing()


if __name__ == "__main__":

    menu = Menu()
    menu.Inicio()
