tamanhoVet = int(input("Informe o tamanho do vetor: "))
numeros = [0] * tamanhoVet
calculo = 0
media = 0
maior = 0
menor = 0

for i in range(0, len(numeros)):
    numeros[i] = int(input(f"Agora informe o {i + 1} valor: "))
    calculo += numeros[i]
    media += numeros[i] / tamanhoVet
    if(numeros[i] > maior):
        maior = numeros[i]
    elif(numeros[i] < menor):
        menor = numeros[i]


print(f"Números: {numeros}")
print(f"Ordem inversa dos números: {numeros[::-1]}")
print(f"Soma de todos os elementos: {calculo}")
print(f"A média aritmética de todos os números é: {media}")
print(f"Números que estáo em índices pares: {numeros[::2]}")
print(f"O número no índice {i} é o maior número: {maior}")
print(f"O número no índice {i} é o menor número: {numeros[i]}")
print(f"tem {len(numeros[::2])} pares e tem {len(numeros[::3])} impares")
