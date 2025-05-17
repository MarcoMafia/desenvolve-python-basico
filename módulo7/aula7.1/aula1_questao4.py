numero = input("Digite o número: ")
if numero.isdigit() :
    if len(numero) == 8:
        numero = "9" + numero
        print (numero[:5] + "-" + numero[5:])
    elif len(numero) == 9:
        if numero[0] == "9":
            print (numero[:5] + "-" + numero[5:])
        else: 
            print("O número é inválido!")
else:
    print("Digite apenas números")