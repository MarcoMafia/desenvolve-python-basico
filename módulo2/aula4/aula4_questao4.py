#4 - Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas 
#necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. 
#A saída deve estar formatada exatamente como indicado.

##Entrada
576
##Saída
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00

valor= int(input("Digite o valor, em reais:"))
notas100= int(valor/100)
valor = valor - notas100 *100
notas50= int(valor/50)
valor = valor - notas50 *50
notas20= int(valor/20)
valor = valor - notas20 *20
notas10= int(valor/10)
valor = valor - notas10 *10
notas5= int(valor/5)
valor = valor - notas5 *5
notas2= int(valor/2)
valor = valor - notas2 *2
notas1= int(valor/1)
valor = valor - notas1 *1
print (notas100, "nota(s) de 100\n",notas50, "nota(s) de 50\n",notas20, "nota(s) de 20\n", notas10, "nota(s) de 10\n",notas5,  "nota(s) de 5\n",notas2, "nota(s) de 2\n",notas1, "nota(s) de 1")
