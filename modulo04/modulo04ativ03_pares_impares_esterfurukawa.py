numeros = [12, 7, 19, 24, 8, 3, 15, 30, 41, 50]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Conjunto original: {numeros}")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")