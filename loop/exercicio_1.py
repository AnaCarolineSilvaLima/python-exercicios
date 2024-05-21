n=int(input("Digite quantos números você quer calcular na média: "))
soma = 0
iteracao = 1
while iteracao<=n:
    numero = float(input("Digite um número: "))
    soma += numero
    iteracao += 1
print(f"A média é igual a {soma/n}")    