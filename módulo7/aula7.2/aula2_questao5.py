import random
def embaralhar_letras(palavra):
    if len(palavra) <= 3:
        return palavra
    else:
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_letras(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)
frase = input("Digite uma frase: ")
resultado = embaralhar_palavras(frase)
print(resultado)