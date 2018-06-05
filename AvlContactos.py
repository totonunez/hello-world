class AVLContacto(object):
    def __init__(self):
        self.root = None
        self.hojas = 0

        
    def agregarContacto(self):
        print("Agregar nombre: ")
        nombre = input()
        print("Agregar apellido: ")
        apellido = input()
        print("Agregar telefono: ")
        telefono = input()
        print("Agregar email: ")
        email = input()
        nuevo = ContactoArbol(nombre,apellido,telefono,email)
        return self.add(nuevo)
    
    def __add(self, root, contacto):
        if  root == None:
            return contacto
        elif contacto.apellido < root.apellido:
            root.left = self.__add(root.left, contacto)
        else:
            root.right = self.__add(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),
        self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    
    def add(self,contacto):
        if self.root:
            self.__add(self.root,contacto)
        else:
            self.root = contacto
            
    def getBalance(self, root):
        if not root:
          return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
        self.getHeight(y.right))
        # Return the new root
        return y

