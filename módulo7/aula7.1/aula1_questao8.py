import re

cpf_usuario = input("Digite o CPF no formato XXX.XXX.XXX-XX: ") 
if re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf_usuario):
    cpf_sem_ponto = cpf_usuario.replace(".", "").replace("-", "")

    multiplicador = 10
    resultado = 0
    for digito in cpf_sem_ponto[0:9]:
        resultado += int(digito) * multiplicador
        multiplicador -= 1

    resto = resultado % 11
    dv1 = 0 if resto < 2 else 11 - resto
    cpf_verificado1 = cpf_sem_ponto[:9] + str(dv1)

    multiplicador = 11
    resultado = 0
    for digito in cpf_verificado1[:10]:
        resultado += int(digito) * multiplicador
        multiplicador -= 1

    resto = resultado % 11
    dv2 = 0 if resto < 2 else 11 - resto
    cpf_verificado2 = cpf_verificado1 + str(dv2)

    if cpf_verificado2 == cpf_sem_ponto:
        print("CPF Válido")
    else:
        print("CPF Inválido")
else:
    print("Formato de CPF inválido")