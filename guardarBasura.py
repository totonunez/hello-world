'''
    def sacarContacto(self):

        aux = self.head
        while aux:
            if nombre == aux.nombre and apellido == aux.apellido:
                return aux
            aux = aux.next
        print("El nodo no existe")
        return None


        delete = self.find()
        if delete:
            self._eliminarContacto(self.delete)
        else:
            print("No se encuentra registrada esta persona")
            print("Desea agregar el contacto?")
            var=3
            while var != 1 or var != 2:
                var = input(print("Presione: SI: 1 , NO: 2"))
                if var == 1:
                    self.agregarContacto()
                elif var == 2:
                    pass
                else:
                    print("Porvafor vuelva a agregar una opción valida")
                    pass



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
'''
