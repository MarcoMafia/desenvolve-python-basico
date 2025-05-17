def eh_anagrama(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2)

def encontrar_anagramas(frase, palavra_objetivo):
    palavras = frase.split()
    anagramas = []

    for palavra in palavras:
        if len(palavra) == len(palavra_objetivo) and eh_anagrama(palavra, palavra_objetivo):
            anagramas.append(palavra)

    return anagramas

# Entrada do usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

resultado = encontrar_anagramas(frase, palavra_objetivo)

print("Anagramas:", resultado)
