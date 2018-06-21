from faker import Faker
fake = Faker()

#for i in range(10):
    #print(fake.name()," ",fake.email())
x=fake.name()

def nombre(x):
    return sum( for i in x)

print(nombre(x))

            
    
