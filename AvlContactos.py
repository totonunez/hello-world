#import random, math

outputdebug = False

def debug(msg):
    if outputdebug:
        print(msg)

class ContactoAvl():
    def __init__(self, nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.left = None
        self.right = None


class AVLTree():
    def __init__(self, *args):
        self.root = None
        self.height = -1
        self.balance = 0

        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.root:
            return self.root.height
        else:
            return 0

    def is_leaf(self):
        return (self.height == 0)

    def insert(self, contacto):
        tree = self.root

        if tree == None:
            self.root = contacto
            self.root.left = AVLTree()
            self.root.right = AVLTree()
            debug("El Contacto incertado [" + str(contacto.apellido) + "]")

        elif contacto.apellido < self.root.apellido:
            self.root.left.insert(contacto)

        elif contacto.apellido > self.root.apellido:
            self.root.right.insert(contacto)

        else:
            debug("El contacto incertado [" + str(contacto.apellido) + "] ya está en el arbol.")

        self.rebalance()

    def agregarContacto(self):
        return contacto

    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()



    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotar contacto de apellido ' + str(self.root.apellido) + ' derecho')
        A = self.root
        B = self.root.left.root
        T = B.right.root

        self.root = B
        B.right.root = A
        A.left.root = T

    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotar contacto de apellido ' + str(self.root.apellido) + ' izquierdo')
        A = self.root
        B = self.root.right.root
        T = B.left.root

        self.root = B
        B.left.root = A
        A.right.root = T


    def update_heights(self, recurse=True):
        if not self.root == None:
            if recurse:
                if self.root.left != None:
                    self.root.left.update_heights()
                if self.root.right != None:
                    self.root.right.update_heights()

            self.height = max(self.root.left.height,
                              self.root.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.root == None:
            if recurse:
                if self.root.left != None:
                    self.root.left.update_balances()
                if self.root.right != None:
                    self.root.right.update_balances()

            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0

    def delete(self,contacto):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.root != None:
            if self.root.apellido == contacto.apellido and self.root.nombre == contacto.nombre:
                debug("Eliminar el Contacto con nombre  " + contacto.nombre + " y " + contacto.apellido)
                if self.root.left.root == None and self.root.right.root == None:
                    self.root = None # leaves can be killed at will

                # Si el contacto que encontramos solo tiene un subarbol
                elif self.root.left.root == None:
                    self.root = self.root.right.root
                elif self.root.right.root == None:
                    self.root = self.root.left.root

                # peor caso: El subarbol que encontramos tiene ambos hijos , encontrar el successo
                else:
                    replacement = self.logical_successor(self.root)
                    if replacement != None:
                        debug("Se logró encontrar y se reemplazará por: " + nombre  + " y " + apellido + " -> " + replacement.apellido)
                        self.root.nombre = replacement.nombre
                        self.root.apellido = replacement.apellido
                        self.root.telefono = replacement.telefono
                        self.root.email = replacement.email

                        # replaced. Now delete the key from right child
                        self.root.right.delete(replacement)

                self.rebalance()
                return
            elif contacto.apellido < self.root.apellido:
                self.root.left.delete(contacto)
            elif contacto.apellido > self.root.apellido:
                self.root.right.delete(contacto)

            #Recordar siempre balancear al final
            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        '''
        Find the biggest valued node in LEFT child
        '''
        node = node.left.root
        if node != None:
            while node.right != None:
                if node.right.root == None:
                    return node
                else:
                    node = node.right.root
        return node

    def logical_successor(self, node):
        '''
        Find the smallese valued node in RIGHT child
        '''
        node = node.right.root
        if node != None: # just a sanity check

            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.root == None:
                    return node
                else:
                    node = node.left.root
        return node

    def check_balanced(self):
        if self == None or self.root == None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())

    def inorder_traverse(self):
        if self.root == None:
            return []

        inlist = []
        l = self.root.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.root.apellido)

        l = self.root.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, level=0, pref=''):
        '''
        Deplegar completamente los apellido de todo el arbol de manera recursiva.
        TODO: crear una mejor demostración para poder demostrar todas las cosas.
        '''
        self.update_heights()  # Primero se requiere actualizar la altura antes
                               # Rebalancear el arbol
        self.update_balances()
        if(self.root != None):
            print( "-" * level * 2, pref, self.root.nombre , self.root.apellido, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.root.left != None:
                self.root.left.display(level + 1, '<')
            if self.root.left != None:
                self.root.right.display(level + 1, '>')

    def ingresarNContactos(self,n):
        from faker import Faker
        from random import randint
        fake = Faker()
        for i in range(0,n):
            nombreCompleto=fake.name()
            email = fake.email()
            telefono = str(randint(11111111,99999999))
            nuevo = ContactoAvl(nombreCompleto.split()[0],nombreCompleto.split()[1],telefono,email)
            self.insert(nuevo)

        return True

    def buscarContacto(self):
         print("Agregar nombre: ")
         nombre = input()
         print("Agregar apellido: ")
         apellido = input()
         buscado = ContactoAvl(nombre,apellido,None,None)
         return buscado


                
    def __search(self, contacto, tree):
        if contacto.apellido == tree.apellido:
            print("Nodo Encontrado")
        elif contacto.apellido < tree.apellido:
            self.__search(contacto, tree.left.root)
        else:
            self.__search(contacto, tree.right.root)

    def search(self, contacto):
        if self.root == None:
            print("El arbol está vacio")
            return False
        else:
            self.__search(contacto, self.root)
            
# Usage example
if __name__ == "__main__":
    
    listaAvl = AVLTree()
    n=int(input("Agregar la cantidad de contactos en su estructura: "))
    from time import time
    inicio = time()
    print ("----- Inserting -------")
    listaAvl.ingresarNContactos(n)
    lastTime = time() - inicio
    print(lastTime)

    listaAvl.display()
    buscado = listaAvl.buscarContacto()
    inicio = time()
    listaAvl.search(buscado)
    #listacontactos.eliminarContacto(None,listacontactos.head,buscado)
    lastTime = time() - inicio
    print("El tiempo de busqueda en", n ,"contactos es de" ,lastTime, "segundos")
