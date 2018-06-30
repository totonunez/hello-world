from faker import Faker
from time import time
fake = Faker()

inicio = time()

for i in range(10):
    print(fake.name()," ",fake.email())

lapsoTiempo = time() - inicio
print(lapsoTiempo)

#for i in range(0,10):
 #   x=fake.name()
  #  a,b=x.split()

    



#y = fake.name()
#a,b=y.split()
