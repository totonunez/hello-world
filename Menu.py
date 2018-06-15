class Menu:
    def __init__(self):
        self.head = None
        self.count = 0

    def Inicio(self):
        print("Bienvenido a su lista de contactos \nIngrese la lista que desee implementar en sus Contactos")
        print("1. Lista de Contacto")
        print("2. Arbol Binario")
        print("3. AVL")
        print("4. Arbol_2_3")
        print("5. Hashing")
        op=int(input("Ingrese opcion: "))
        if op==1:
            self.ListaContactos()
        elif op==2:
            self.ArbolBinario()
        elif op==3:
            self.AVL()
        elif op==4:
            self.Hashing()
        else:
            print("A ingresado una opción no valida, por favor vuelva a ingresar opcion")
            self.Inicio()

    def Lista(sef):
        print("Ha ingresado la lista de contactos, ingrese su opción")
        print("1. Ingresar")
        print("2. Eliminar")
        print("3. Desplegar Contactos")
        print("0. Volver al Menu Anterior")

        op=int(input("Ingrese opcion: "))
        if op==1:
            if self.cont==0:
                self.head = ListaContactos()
            self.head.IngresarContacto()
            self.cont +=1
            
        elif op==2:
            if self.cont < 1:
                print("No puede eliminar Contactos, dado que no hay ninguno")
            else:
                self.head.EliminarContacto()
                self.cont -=1

        elif op==3:
            if self.cont < 1:
                print("No se encuentran Contactos disponible, porfavor ingrese otra opcion")
                

    def ArbolBinario(self):
        print()
                
    

if __name__ == "__main__":
    
    menu = Menu()
    menu.Inicio()
