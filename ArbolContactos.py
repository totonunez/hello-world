from ClaseContactoArbol import *

class ArbolContactos:
    def __init__(self):
        self.root = None
        self.hojas = 0

    def getVacio(self):
        return self.root == None

    def __add(self, contacto, brunch):
        if brunch == contacto:
            print("Este nodo ya existe")
        else:
            if contacto.apellido < brunch.apellido:
                if brunch.left == None:
                    brunch.left = contacto
                    brunch.left.parent = brunch
                else:
                    self.__add(contacto, brunch.left)
            elif contacto.apellido > brunch.apellido:
                if brunch.right == None:
                    brunch.right = contacto
                    brunch.right.parent = brunch
                else:
                    self.__add(contacto, brunch.right)

    def add(self, contacto):
        if self.getVacio():
            self.root = contacto
        else:
            self.__add(contacto, self.root)

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


    def eliminarContacto(self):
        nombre=input("Ingrese nombre de la persona que desee eliminar \n ")
        apellido=input("Ingrese apellido de la persona que desee eliminar \n ")
        delete = ContactoArbol(nombre,apellido,None,None)
        borrar = self.search(delete)
        if borrar:
            self.deleteContacto(borrar)
        else:
            print("No se han encontrado contactos")
            print("PORFAVOR VUELVA A INGRESAR DATOS")
            self.eliminarContacto()

    def buscarContacto(self):
        nombre=input("Ingrese nombre de la persona que desee eliminar \n ")
        apellido=input("Ingrese apellido de la persona que desee eliminar \n ")
        buscado = ContactoArbol(nombre,apellido,None,None)
        self.search(buscado)


    def __search(self, contacto, brunch):
        if brunch == None:
            print('gg no existe tu Contacto')
            return None
        elif contacto.nombre == brunch.nombre and contacto.apellido == brunch.apellido:
            print('iziPizie')
            return brunch
        elif contacto.apellido < brunch.apellido and brunch.left != None:
            self.__search(contacto, brunch.left)
        elif contacto.apellido > brunch.apellido and brunch.right != None:
            self.__search(contacto, brunch.right)

    def search(self, contacto):
        if self.getVacio():
            print("No hay contactos en la lista")
            return None
        else:
            return self.__search(contacto, self.root)


    def deleteContacto(self, contacto):
        def min_value_contacto(n):
            current = n
            while current.left != None:
                current = current.left
            return current

        def number_children(n): # Return the number of childrens of the node to be deleted
            number_children = 0
            if n.left != None:
                number_children += 1
            if n.right != None:
                number_children += 1
            return number_children

        node_parent = contacto.parent # Get the parent of the node to be deleted
        node_children = number_children(contacto)

        # Case 1: Deleting a node without childrens
        #Lo que hace node.parent es retornar el nodo que apunta al hijo, y retornar por quien es apuntado
        if node_children == 0:
            if node_parent.left == contacto:
                node_parent.left = None
            else:
                node_parent.right = None

            if contacto == self.root:
                self.root = None

        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if contacto.left != None:
                child = contacto.left
            else:
                child = contacto.right

            # Replace the node to be deleted with its child
            if contacto is not self.root:

                if node_parent.left == contacto:
                    node_parent.left = child
                else:
                    node_parent.right = child

                # Change the parent of the child
                child.parent = node_parent

            else:
                self.root=child
                child.parent=None


        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_value_node(contacto.right) # Get the inorder successor of the deleted node
            contacto.nombre = successor.nombre
            contacto.apellido = successor.apellido
            contacto.telefono = successor.telefono
            contacto.mail = successor.mail # Copia los valores generales del nodo completamente
            self.delete_node(successor)



    def InOrder(self,root):
        if root is None:
            pass
        else:
            self.InOrder(root.left)
            root.getInformacion()
            print("")
            self.InOrder(root.right)



    def _tree_height(self, current, height):
        if current == None:
            return height
        left_height = self._tree_height(current.left, height+1)
        right_height = self._tree_height(current.right, height+1)
        return max(left_height, right_height)#luego de haber obtenido la profundidad de todos los arboles, se logra comprender la manera
        # de como tiene que seleccionar una y otra ves cual es el mayor de las profundidades de todos los nodos y buscará siempre el mayor de
        # todos los mayores

    def tree_height(self): #Implementar
        if self.empty():
            return 0
        else:
            return self._tree_height(self.root, 0)

    def node_height(self, contacto): #Implementar
        brunch = self.root
        height = 0
        if self.search(contacto):
            height += 1
            while brunch.nombre != contacto.nombre and brunch.apellido != contacto.apellido:
                if contacto.apellido < brunch.apellido:
                    brunch = brunch.left
                else:
                    brunch = brunch.right
                height += 1
            print("La altura de el nodo ingresado es de: ",height)
        return False

    def find_minimum(self): #encuentra el menor valor del arbol
        if self.empty():
            return False
        else:
            self.__find_minimum(self.root)

    def __find_minimum(self, node):

        if node.left is None:
            print("El minimo valor es ", node.value)
        else:
            self.__find_minimum(node.left)

    def find_maximo(self): #encuentra el menor valor del arbol
        if self.empty():
            print ("El arbol maldito está cochinamente vacio ")
            return False
        else:
            self.__find_maximo(self.root)

    def __find_maximo(self, node):

        if node.right is None:
            print("El máximo valor es ", node.value)
        else:
            self.__find_maximo(node.righ)

    def ingresarNContactos(self,n):
        from faker import Faker
        from random import randint
        fake = Faker()
        for i in range(0,n):
                nombreCompleto=fake.name()
                email = fake.email()
                telefono = str(randint(11111111,99999999))
                nuevo = ContactoArbol(nombreCompleto.split()[0],nombreCompleto.split()[1],telefono,email)
                self.add(nuevo)

        return True

if __name__ == "__main__":

    tree = ArbolContactos()
    n=int(input("Agregar la cantidad de contactos en su estructura: "))
    from time import time
    inicio = time()
    print ("----- Inserting -------")
    tree.ingresarNContactos(n)
    lastTime = time() - inicio
    #tree.InOrder(tree.root)
    print("El tiempo de ejecución de los programas es de: ", lastTime)
