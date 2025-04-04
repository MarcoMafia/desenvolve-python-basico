'''
4 - Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês.
O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. 
Reescreva esse código usando apenas duas variáveis.
'''
juros = 0.01
saldo = 500
saldo = saldo * (1 + juros )**3
print ("Após 3 meses meu novo saldo é:")
print (saldo)