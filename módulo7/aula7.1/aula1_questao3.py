frase = input("Digite a frase: ")
branco = 0
for caractere in frase:
    if caractere == " ":
      branco += 1
print("Espaços em branco: ", branco)