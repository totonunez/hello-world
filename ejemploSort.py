class caja:
    def __init__(self,dato):
        self.dato = dato

    def getInfo(self):
        print(self.dato)

class Fila:
    def __init__(self,n):
        self.lista = [None]*n
        self.n = n

    def cambiar(self):
        for i in range(0,self.n):
            x = self.lista[i]
            j = i-1
            while j >=0 and self.lista[j].dato > x.dato:
                self.lista[j+1] = self.lista[j]
                j=j-1
            self.lista[j+1]=x


lista = Fila(5)
y = [3,6,1,4,2]

for i in range(0,5):
    lista.lista[i] = caja(y[i])

x.cambiar()
