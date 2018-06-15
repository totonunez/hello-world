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

    def __search(self, contacto, node):
        if node == None:
            print('gg')
            return None
        elif contacto.nombre == brunch.nombre and contacto.apellido == brunch.apellido:
            print('iziPizie')
            return node 
        elif contacto.apellido < brunch.apellido and brunch.left != None:
            self.__search(contacto, brunch.left)
        elif contacto.apellido > brunch.apellido and brunch.right != None:
            self.__search(contacto, brunch.right)

    def search(self, contacto):
        if self.empty():
            return None
        else:
            return self.__search(value, self.root)
            
                    
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

        node_parent = node.parent(contacto) # Get the parent of the node to be deleted
        node_children = number_children(contacto)

        # Case 1: Deleting a node without childrens
        #Lo que hace node.parent es retornar el nodo que apunta al hijo, y retornar por quien es apuntado
        if node_children == 0:
            if node_parent.left == contacto:
                node_parent.left = None
            else:
                node_parent.right = None
        # Case 2: Deleting a node with one children
        if node_children == 1:
            # Get the children of the node to be deleted
            if contacto.left != None:
                child = contacto.left
            else:
                child = contacto.right

            # Replace the node to be deleted with its child
            if node_parent.left == contacto:
                node_parent.left = child
            else:
                node_parent.right = child

            # Change the parent of the child
            child.parent = node_parent
        # Case 3: Deleting a node with two childrens
        if node_children == 2:
            successor = min_value_node(contacto.right) # Get the inorder successor of the deleted node
            contacto = successor # Copia los valores generales del nodo
            self.delete_node(successor)


    def InOrder(self,root):
        if root is None:
            pass
        else:
            self.InOrder(root.left)
            print(root.getInformacion)
            self.InOrder(root.right)

    def PostOrder(self,root):
        if root is None:
             pass
        else:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.getInformacion)

    def PreOrder(self, root):
        if root is None:
            pass
        else:
            print(root.getInformacion)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    def leaf_number(self,root): #Calcula el numero de hojas que hay en el arbol
        if root is None:
            pass
        else:
            if root.left & root.right is None:
                self.hojas  += 1
            self.leaft_numer(root.left)
            self.leaft_numer(root.right)

        print('El número total de hojas en el arbol es de ', self.hojas)

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

    def node_height(self, value): #Implementar
        node = self.root
        height = 0
        if self.search(value):
            height += 1
            while node.value != value:
                if value < node.value:
                    node = node.left
                else:
                    node = node.right
                height += 1
            return height
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
            self.__find_maximo(node.right)