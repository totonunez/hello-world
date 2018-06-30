from time import time
def test():
    for i in range(1):
        print("Hello, world!".replace("Hello", "Goodbye"))


inicio = time()
test()
lapsoTiempo = time() - inicio
print(lapsoTiempo)

'''
DEBEMOS EMPLEAR EL USO DEL LAPSUS DE TIEMPO PARA PODER REALIZAR EL ANALISIS COMLETO DE
CUANTO ES QUE DEMORA REALIZARSE TODA LA DEPURACION
'''
