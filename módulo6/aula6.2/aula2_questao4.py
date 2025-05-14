i_lista1= int(input("Digite a quantidade de elementos da lista 1: "))
lista1= list()
print(f"Digte os {i_lista1} elementos da lista 1: ")
for i in range (i_lista1):
    elementos = int(input())
    lista1.append(elementos)
i_lista2= int(input("Digite a quantidade de elementos da lista 2: "))
lista2= list()
print(f"Digte os {i_lista2} elementos da lista 2: ")
for i in range (i_lista2):
    elementos = int(input())
    lista2.append(elementos)
lista_combinada= list()
min_len = min(len(lista1), len(lista2))
for i in range(min_len):
    lista_combinada.append(lista1[i])
    lista_combinada.append(lista2[i])
if len(lista1) > len(lista2):
    lista_combinada.extend(lista1[min_len:])
else:
    lista_combinada.extend(lista2[min_len:])
print ("Lista intercalada: ",lista_combinada)