from ClaseContacto import *

class Lista:
        #Constructor de lista
    def __init__(self):
       self.head=None
       self.last=None

    def getVacio(self):
        if self.head==None:
            return True
        
    def agregarInicio(self,nuevoContacto):
        
        if self.getVacio()==True:
            self.head=self.last=nuevoContacto
        else:
            nuevoContacto.next=self.head
            self.head=nuevoContacto

    def agregarFinal(self,nuevoContacto):
    
        if self.getVacio()==True:
            self.head=self.last=nuevoContacto
        else:
            self.last.next=nuevoContacto
            self.last=nuevoContacto

    def agregarOrden(self,nuevoContacto):

        if self.getVacio() == True:
            self.head = self.last = nuevoContacto
        else:
            aux = self.head
            
            if self.head.apellido > nuevoContacto.apellido:
                nuevoContacto.next = self.head
                self.head = nuevoContacto
            else:
                while aux:
                    if nuevoContacto.apellido > aux.apellido:
                        nuevoContacto.next = aux.next
                        aux.next=nuevoContacto
                        if self.last.next is True:
                            self.last = nuevoContacto
                        break
                    else:
                        aux=aux.next

    def eliminarContacto(self,nombre,apellido):
        


    def invertir(self):
        while self.head.next:
            aux=self.head
            while aux.next.next:
                aux=aux.next
            aux.next.next=aux
            aux.next=None

        aux=self.head
        self.head=self.last
        self.last=aux
        
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

    


    
