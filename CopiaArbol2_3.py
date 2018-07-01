class Data():
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono= telefono
        self.email=email

    def getInformacion(self):
        print("Nombre: {}, Apellido: {},Telefono: {},email: {} \n".format(self.nombre, self.apellido, self.telefono, self.email))

class NodoContacto23(object):

    def __init__(self, contacto , par = None):
        self.data =list([contacto])
        self.parent = par
        self.child = list()
'''
    def __str__(self):
	    if self.parent:
    		return str(self.parent.data) + ' : ' + str(self.data)
    	    print('Root : ' + str(self.data))

    def __lt__(self, node):
	    return self.data[0].apellido < node.data[0].apellido
'''
    def _isLeaf(self):
        return len(self.child) == 0

	# merge new_node sub-tree into self node
    #print ("Node _add: " + str(new_node.data) + ' to ' + str(self.data))
    def _add(self, new_node):
        for child in new_node.child:
            child.parent = self
    	self.data.extend(new_node.data)
    	self.data.sortContactos(len(self.data))
    	self.child.extend(new_node.child)
    	if len(self.child) > 1:
            self.child.sortContactos(len(self.child))
        if len(self.data) > 2:
            self._split()

	# find correct node to insert new node into tree
    def _insert(self, new_node):
        # print ('Node _insert: ' + str(new_node.data) + ' into ' + str(self.data))

		# leaf node - add data to leaf and rebalance tree
        if self._isLeaf():
            self._add(new_node)

            # not leaf - find correct child to descend, and do recursive insert
        elif new_node.data[0].apellido > self.data[-1].apellido:
            self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0].apellido < self.data[i].apellido:
					self.child[i]._insert(new_node)
					break

	# 3 items in node, split into new sub-tree and add to parent
    def _split(self):
        # print("Node _split: " + str(self.data))
	left_child = Contacto23(self.data[0], self)
	right_child = Contacto23(self.data[2], self)
	if self.child:
            self.child[0].parent = left_child
	    self.child[1].parent = left_child
	    self.child[2].parent = right_child
	    self.child[3].parent = right_child
        left_child.child = [self.child[0], self.child[1]]
	right_child.child = [self.child[2], self.child[3]]

	self.child = [left_child]
	self.child.append(right_child)
	self.data = [self.data[1]]

		# now have new sub-tree, self. need to add self to its parent node
	if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
	    self.parent._add(self)
	else:
            left_child.parent = self
	    right_child.parent = self

	# find an item in the tree; return item, or False if not found
    def _find(self, contacto):
        # print ("Find " + str(item))
	if contacto in self.data:
            return contacto
	elif self._isLeaf():
            return False
	elif contacto.apellido > self.data[-1].apellido:
            return self.child[-1]._find(contacto)
	else:
            for i in range(len(self.data)):
                if contacto < self.data[i].apellido:
                    return self.child[i]._find(contacto)

    def _remove(self, item):
	pass

	# print preorder traversal
    def _preorder(self):
        print(self.data.apellido)
	for child in self.child:
            child._preorder()

    def sortContactos(self,n):
        for i in range(0,n):
            x = self.data[i]
            j = i-1
            while j >=0 and self.data[j].apellido > x.apellido:
                self.data[j+1] = self.data[j]
                j=j-1
            self.data[j+1]=x



class Tree23:
        #Recordar que el atributo data es encargado de ser y estar estructurado como
        #una clase data capaz de todo

	def __init__(self):
		print("Inicializar el arbol en Nulo")
		self.root = None

	def insert(self, nuevo):
        #Recuerda que le incertamos data de clase Data que contiene
        #La información completa de los contactos
        print("Ingresar el dato:", nuevo.data[0].nombre ,"",nuevo.data[0].apellido)
		if self.root is None:
			self.root = nuevo
		else:
			self.root._insert(nuevo)
			while self.root.parent:
				self.root = self.root.parent
		return True

	def find(self, data):
		return self.root._find(data)

	def remove(self, data):
		self.root.remove(data)

	def print2primerasAlturas(self):
		print ('----Cumbre de alturas----')
		print (str(self.root.data.getInformacion()))
		for child in self.root.child:
			print (str(child.data.getInformacion()), end=' ')
		print(' ')


    def preorder(self):
		print ('----Preorder----')
		self.root._preorder()


    def ingresarData(self,nombre,apellido,telefono,email):
        contacto = Data(nombre,apellido,telefono,email)
        return contacto


    def ingresarNContactos(self,n):
        from faker import Faker
        from random import randint
        fake = Faker()

        for i in range(0,n):
            nombreCompleto=fake.name()
            email = fake.email()
            telefono = str(randint(11111111,99999999))
            nuevo = Data(nombreCompleto.split()[0],nombreCompleto.split()[1],telefono,email)
            self.insert(Contacto23(nuevo))

        return True


'''
tree = Tree23()
inicio = time()
input("Agregar la cantidad de contactos en su estructura: ")
tre.ingresarNContactos(n)
lastTime = time() - inicio
print("lastTime")
tree.preorder()
'''
