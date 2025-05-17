import random
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
n = random.randint(1,10)
def criptografar(nomes, n):
    nomes_criptografados = []
    for palavra in nomes:
        palavra_criptografada = ""
        for letra in palavra:
            numero_letra = ord(letra)
            letra_criptografada = chr (numero_letra + n)
            palavra_criptografada += letra_criptografada
        nomes_criptografados.append(palavra_criptografada)
    return nomes_criptografados

nomes_criptografados = criptografar(nomes, n)
print("Chave Aleatória: ", n)
print("Nomes criptografados: ", nomes_criptografados)
