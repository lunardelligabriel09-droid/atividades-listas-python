
frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
numeros = [10, 25, 3, 47, 8, 15, 30]

print(frutas[0])
print(frutas[len(frutas) - 1])

print(frutas[0])
print(frutas[-1])

frutas.append('kiwi')
frutas.insert(2, 'morango')
frutas.remove('banana')

for numero in numeros:
    if numero > 15:
        print(numero)

print(sorted(numeros))
print(sorted(numeros, reverse=True))