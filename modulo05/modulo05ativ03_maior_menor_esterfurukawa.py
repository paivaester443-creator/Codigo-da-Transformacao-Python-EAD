def maior_menor(numeros):
    if not numeros:
        return None, None
    return max(numeros), min(numeros)

lista = [14, 2, 88, -5, 42, 10]
maior, menor = maior_menor(lista)
print(lista)

print(f"Maior: {maior} | Menor: {menor}")
