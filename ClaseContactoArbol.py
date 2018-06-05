class ContactoArbol:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.left = None
        self.right = None
        self.parent = None

    def getInformacion(self):
        print("Nombre: ",self.nombre)
        print("Apellido: ",self.apellido)
        print("Número de Telefono: ",self.telefono)
        print("Email: ",self.email)
