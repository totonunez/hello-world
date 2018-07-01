from ClaseContacto import *

class ListaContactos:
        #Constructor de lista
    def __init__(self):
       self.head=None

    def getVacio(self):
        return self.head==None


    def agregarContacto(self):
        print("Agregar nombre: ")
        nombre = input()
        print("Agregar apellido: ")
        apellido = input()
        print("Agregar telefono: ")
        telefono = input()
        print("Agregar email: ")
        email = input()
        nuevo = Contacto(nombre,apellido,telefono,email)
        return self.agregarOrden(nuevo)

    def buscarContacto(self):
        print("Agregar nombre: ")
        nombre = input()
        print("Agregar apellido: ")
        apellido = input()
        buscado = Contacto(nombre,apellido,None,None)
        return buscado

    def agregarOrden(self,nuevoContacto):
        if self.getVacio():
            self.head = nuevoContacto
        else:
            if nuevoContacto.apellido > self.head.apellido:
                prev=self.head
                aux=prev.next
                while prev:
                    if nuevoContacto.apellido > prev.apellido:
                        nuevoContacto.next = aux
                        prev.next = nuevoContacto
                        break
                    else:
                        prev = aux
                        aux=aux.next
            else:
                #Agregar en la cabeza
                nuevoContacto.next=self.head
                self.head = nuevoContacto


    def Eliminar(self):
        print("Debe Ingresar nombre y apellido del contacto de busca")
        print("Ingrese nombre")
        nombre = input()
        print("Ingrese apellido")
        apellido = input()
        eliminar = Contacto(nombre,apellido,None,None)
        self.eliminarContacto(None,self.head,eliminar)

    def eliminarContacto(self,prev,aux,eliminado):
        if eliminado.nombre == aux.nombre and eliminado.apellido == aux.apellido:
            if prev==None:
                self.head = aux.next
            else:
                prev.next=aux.next
            print("Se a logrado encontrar el contacto")
        else:
            prev = aux
            aux = aux.next
            if aux==None:
                print("No se a podido encontrar el contacto solisitado")
            else:
                self.eliminarContacto(prev,aux,eliminado)
            #esta funcion debe
            #se debe iniciar en self.matar(None,self.head,contacto)


    def printList(self):
        if self.getVacio():
             print("Lista vacia")
        else:
            aux = self.head
            while aux:
                print("Nombre: {}, Apellido: {},Telefono: {},email: {} \n".format(aux.nombre, aux.apellido, aux.telefono, aux.email))
                aux = aux.next


    def agregarNContactos(self,n):
        from faker import Faker
        from random import randint
        from time import time
        fake = Faker()
        inicio = time()
        for i in range(0,n):
                nombreCompleto=fake.name()
                email = fake.email()
                telefono = str(randint(11111111,99999999))
                nuevo = Contacto(nombreCompleto.split()[0],nombreCompleto.split()[1],telefono,email)
                self.agregarOrden(nuevo)

        lastTime = time() - inicio
        print("El tiempo de incerción de: ", n , "contactos es de , " ,lastTime, " segundos")

    def search(self,prev,aux,buscado):
        if buscado.nombre == aux.nombre and buscado.apellido == aux.apellido:
            #print("Se a logrado encontrar el contacto")
            return aux
        else:
            prev = aux
            aux = aux.next
            if aux==None:
                pass
                #print("No se a podido encontrar el contacto solisitado")
            else:
                self.search(prev,aux,buscado)


'''
    def agregarOrden(self,nuevoContacto):
        if self.getVacio():
            self.head = nuevoContacto
        else:
            aux=self.head
            if nuevoContacto.apellido[0] > aux.apellido[0]:
                while aux:
                    if aux.apellido[0] < nuevoContacto.apellido[0]:
                        nuevoContacto.next = aux.next
                        nuevoContacto.prev = aux
                        if nuevoContacto.next:
                            nuevoContacto.next.prev = nuevoContacto
                        aux.next=nuevoContacto
                        break
                    else:
                        aux = aux.next

            else:
                nuevoContacto.next=aux
                aux.prev = nuevoContacto
                self.head = nuevoContacto
'''
