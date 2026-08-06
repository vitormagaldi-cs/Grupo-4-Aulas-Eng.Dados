numero = 0
soma = 0

for numero in range(1,6):
    numero = float(input(f"Digite o {numero}º número: "))
    soma += numero

media = soma / 5

print(f"A média dos numeros digitados é: {media:.2f}")
