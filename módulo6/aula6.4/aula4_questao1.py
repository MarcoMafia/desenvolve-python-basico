lista = [i for i in range(20, 51)]
print(lista)
num_pares = [l for l in lista if l % 2 == 0] 
print (num_pares)
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
quadrado = [l**2 for l in lista]
print (quadrado)
lista = [i for i in range(1,101)]
div_7 = [l for l in lista if l%7 == 0]
print (div_7)
lista = [i for i in range(0, 30, 3)]
par_impar= ["par" if l % 2 == 0 else "ímpar" for l in lista]
print (lista)
print(par_impar)