d= float (input("Distância da entrega, em km: "))
m= float(input("Peso do pacote, em kg:"))
if d <= 100:
    preco= 1 * m
if d >= 101 and d <= 300 :
    preco= 1.5 * m
if d > 300:
    preco = 2 * m
if m > 10:
    taxa= 10
else:
    taxa = 0
preco_final = preco + taxa
print ("O valor do frete será: ", preco_final)
