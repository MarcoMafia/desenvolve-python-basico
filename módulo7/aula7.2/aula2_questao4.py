def validador_senha(senha):
    if len(senha) < 8:
        return False
    especiais = "@#$%^&+=!"
    maiuscula = False
    minuscula = False
    numero = False
    especial = False
    for caractere in senha:
        if caractere.isupper():
            maiuscula = True
        elif caractere.islower():
            minuscula = True
        elif caractere.isdigit():
            numero = True
        elif caractere in especiais:
            especial = True
    return maiuscula and minuscula and numero and especial
senha = input("Digite a sua senha: ")
print(validador_senha(senha))