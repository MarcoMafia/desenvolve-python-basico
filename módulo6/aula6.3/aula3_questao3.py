import random
original = []
for i in range(20):
    original.append(random.randint(-10, 10))
print("Original: ", original)
max_negativos = 0
melhor_inicio = 0
melhor_fim = 0

for i in range(len(original)):
    for j in range(i + 1, len(original) + 1):
        fatia = original[i:j]
        negativos = sum(1 for x in fatia if x < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            melhor_inicio = i
            melhor_fim = j

del original[melhor_inicio:melhor_fim]

print("Editada: ", original)
