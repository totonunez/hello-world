class Contacto:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.next = None

    def getInformacion(self):
        print("Nombre: ",self.nombre)
        print("Apellido: ",self.apellido)
        print("Número de Telefono: ",self.telefono)
        print("Email: ",self.email)
        
def ingresarNContactos(n):
        from faker import Faker
        from random import randint
        fake = Faker()
        lst = [None]*n
        for i in range(0,n):
                x=fake.name()
                nombre,apellido = x.split()
                email = str(fake.email())
                telefono = int(randint(11111111,99999999))
                lst[i] = Contacto(nombre,apellido,telefono,email)

        return lst

lista = ingresarNContactos(5)


