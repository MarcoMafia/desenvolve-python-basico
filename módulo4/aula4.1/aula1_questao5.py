respondentes= int(input("Digite a quantidade de respondentes: "))
soma = 0 
cont = 0
while cont < respondentes:
    idade= int(input(f"Digite a idade do respondente {cont + 1}: "))
    soma += idade
    cont += 1
media = soma/respondentes
print("A média das idades dos respondentes é: ", media)