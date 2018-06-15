from ClaseContacto import *

class Lista:
        #Constructor de lista
    def __init__(self):
       self.head=None

    def getVacio(self):
        if self.head==None:
            return True
        
    def agregarInicio(self,nuevoContacto):
        if self.getVacio()==True:
            self.head=nuevoContacto
        else:
            nuevoContacto.next=self.head
            self.head=nuevoContacto

    def agregarOrden(self,nuevoContacto):
        if self.getVacio() == True:
            self.head = nuevoContacto
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
                        break
                    else:
                        aux=aux.next

    def eliminarContacto(self,delete):
        if self.find(delete):
            self._eliminarContacto(self.delete)
        else:
            print("No se encuentra registrada esta persona")
            print("Desea agregar el contacto?")
            var=3
            while var != 1 | var != 2:
                var = input(print("Presione: SI: 1 , NO: 2"))
                if var == 1:
                    self.agregarconstacto()
                elif var == 2:
                    pass
                else:
                    print("Porvafor vuelva a agregar una opción valida")
                

    def _eliminarContacto(self,delete):

        if delete==self.head:
            self.head=self.head.next
            self.head.prev=None
        else:
            if delete.next is not None:
                delete.next.prev=delete.prev
            if delete.prev is not None:
                delete.prev.next=delete.next
            if delete == self.head:
                self.head=self.head.next
            gc.collect()
            
        
        
        
    
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

    def printList(self):
        if self.getVacio():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            seguir = True
            while seguir:
                print("Nodo {} contiene: Nombre {}, Apellido {},Telefono {},email {}".format(i, temp.nombre, temp.apellido, temp.telefono, temp.rut))
                temp = temp.next
                i += 1
                if temp == None:
                    break
        
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
