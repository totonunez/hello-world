from ClaseContacto import Contacto
from ListaContactos import ListaContactos

def str2num(contacto):
    return sum([ord(c) for c in contacto.key])

def hashstr(contacto,size):
    return str2num(contacto)%size

class HashContacto:

    def __init__(self,size):
        self.list = [None]*size
        self.size = size

    def put(self,contacto):
        pos = hashstr(contacto,self.size)
        if self.list[pos] is not None:
            #El siguiente ciclo retornará todos los objetios que hay en la listacontactos
            # de el Hash que hay en ese lugar y orden
            buscado = self.list[pos].search(None,self.list[pos].head,contacto)
            if buscado:
                buscado.nombre = contacto.nombre
                buscado.apellido = contacto.apellido
                buscado.telefono = contacto.telefono
                buscado.email = contacto.email
            else:
                self.list[pos].agregarOrden(contacto)
        else:
            self.list[pos] = ListaContactos()
            self.list[pos].agregarOrden(contacto)



 #Si queremos retornar directamente un contacto ingresando una clave,
 #realizaremos una funcion capaz de retornarnos un contacto con una clave

    def getContactoHash(self,key):
        pos = sum([ord(c) for c in key])
        pos = int(pos%self.size)
        aux = self.list[pos].head
        while aux:
            if key == aux.key:
                return aux.getInformacion()
            aux = aux.next

    def agregarNContactos(self,n):
        from faker import Faker
        from random import randint
        fake = Faker()
        for i in range(0,n):
                nombreCompleto=fake.name()
                email = fake.email()
                telefono = str(randint(11111111,99999999))
                nuevo = Contacto(nombreCompleto.split()[0],nombreCompleto.split()[1],telefono,email)
                self.put(nuevo)

        return True

    def printHash(self):
        for i in range(0,self.size):
            if self.list[i] == None:
                pass
            else:
                self.list[i].printList()

    def getEliminarHash(self,key):
        pos = sum([ord(c) for c in key])
        pos = int(pos%self.size)
        aux = self.list[pos].head
        while aux:
            if key == aux.key:
                return aux.getInformacion()
            aux = aux.next
'''
print("HOLA BUENAS AGREGAR DATOS")
size = int(input("Agregar el tamaño de el arreglo de su lista de contactos de Hash: "))
hash = HashContacto(size)
n=int(input("Agregar la cantidad de contactos en su estructura: "))
from time import time
inicio = time()
print ("----- Inserting -------")
hash.ingresarNContactos(n)
lastTime = time() - inicio
print("El tiempo de ejecución de los programas es de: ", lastTime)
hash.printHash()
clave=input("seleccione clave: ")
inicio = time()
hash.getContactoHash(clave)
lastTime = time()-inicio
print(lastTime)
'''
