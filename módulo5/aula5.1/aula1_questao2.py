import random, math
n= int(input())
soma=0
for i in range(n):
   soma += random.randint (0, 100)
print (math.sqrt(soma))