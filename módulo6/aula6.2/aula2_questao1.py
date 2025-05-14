import random
aleatorios = list()
for i in range(20):
   valor = random.randint(-100, 100)
   aleatorios.append(valor)
print(sorted(aleatorios))
print(aleatorios)
print("Índice de maior valor: ", aleatorios.index(max(aleatorios)))
print("Índice de menor valor: ", aleatorios.index(min(aleatorios)))