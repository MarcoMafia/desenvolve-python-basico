import random
num_elementos = random.randint(5, 20)
for i in range(num_elementos):
    elementos = [random.randint(1,10)]
soma = sum(elementos)
media= soma/ num_elementos
print(elementos)
print("Soma dos valores da lista: ",soma)
print("Média dos valores da lista: ",media)