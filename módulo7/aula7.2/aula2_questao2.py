frase = input("Digite uma frase: ")
def frase_mod(frase):
    frase_mod = frase
    for letra in frase:
        if letra in 'aeiouAEIOU':
            frase_mod= frase_mod.replace(letra, '*')
    return frase_mod 
modificada = frase_mod(frase)
print(modificada)