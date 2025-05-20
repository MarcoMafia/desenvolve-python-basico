def limpar_frase(frase):
    return ''.join(letra.lower() for letra in frase if letra.isalnum())
def palindromo(frase):
    frase_limpa = limpar_frase(frase)
    return frase_limpa == frase_limpa [::-1]
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break
    if palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print('"{frase}" não é palíndromo')