numeros = []
print("Digite pelo menos 4 números inteiros. Digite 'sair' para finalizar a inserção.")
while len(numeros) < 4:
    entrada = input("Digite um número inteiro ou 'sair' para terminar: ")
    if entrada == 'sair':
        print("Você precisa digitar pelo menos 4 números.")
        continue
    else:
        num = int(entrada)
        numeros.append(num)
while True:
    entrada = input("Digite um número inteiro ou 'sair' para finalizar: ")  
    if entrada == 'sair':
        break
    else:
        num = int(entrada)
        numeros.append(num)
print("Lista Original: ", numeros)
print("Os três primeiros elementos: ", numeros[:3])
print("Os dois últimos elementos: ", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par: ", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])