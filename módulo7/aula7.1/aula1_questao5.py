frase = input("Digite uma frase: ")
vogais = 0
i = 0
indices = []
for letra in frase:
    i += 1
    if letra in 'aeiouAEIOU':
        vogais += 1
        indices.append(i)
print (vogais," Vogais")

print("Índices ",indices )