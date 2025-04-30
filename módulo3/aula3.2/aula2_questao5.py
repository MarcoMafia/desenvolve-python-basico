genero= input ("Qual o seu gênero? ")
idade = int(input("Qual a sua idade? "))
tempo_servico= int(input("Qual o seu tempo de serviço, em anos? "))
aposentado= ((genero == "Feminino" and idade > 60) or (genero == "Masculino" and idade > 65) or (tempo_servico >= 30) or ((idade >= 60 or idade < 65 ) and tempo_servico >= 25))
if aposentado == True: 
    print("Você já pode se aposentar") 
else: print ("Você ainda não pode se aposentar")
