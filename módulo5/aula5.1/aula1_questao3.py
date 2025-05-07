import random
n_aleatorio= random.randint (1,10)
n= None
while n != n_aleatorio:
    n = int(input("Adivinhe o número entre 1 e 10: "))
    if n == n_aleatorio: 
        print ("Correto! O número é", n_aleatorio)
        break
    elif n > n_aleatorio:
        print("Muito alto, tente novamente!")
        continue
    else:
        print("Muito baixo, tente novamente!")
        continue

