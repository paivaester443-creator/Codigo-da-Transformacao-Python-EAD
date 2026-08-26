def calcular_media(notas, nota_minima=7.0):
    if not notas:
        return "Nenhuma nota foi informada."
    
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= nota_minima else "Reprovado"
    
    return f"Média: {media:.2f} | Status: {status}"

notas_isabelly = [8.0, 7.5, 6.0, 9.0]
print(calcular_media(notas_isabelly))

notas_sarah = [5.0, 6.0, 4.5, 7.0]
print(calcular_media(notas_sarah))
