# Entra de Dados
print("Cálculo de grandezas elétricas\n")
print("1. Tensão (em Volt)\n")
print("2. Resistência (em Ohm)\n")
print("3. Corrente (em Ampére)\n")
grandeza=(input("Qual a grandeza deseja calcular? 1 2 3"))
if grandeza=="1":
    resistencia1=float(input("Informe a resistência"))
    corrente1=float(input("Informe a corrente"))
    tensao1=(corrente1*resistencia1)
    print(f"A sua tensão é de {tensao1} Volt")
elif grandeza=="2":
    tensao2=float(input("Informe sua tensão: "))
    corrente2=float(input("Informe sua corrente: "))
    resistencia2=(tensao2/corrente2)
    print(f"A sua resitência é de {resistencia2} Ohm")
elif grandeza=="3":
    tensao3=float(input("Informe sua tensão: "))
    resistencia3=float(input("Informe sua resistência: "))
    corrente3=(tensao3/resistencia3)
    print(f"A sua corrente é de {corrente3} Ampére")
else:
    print(f"Número invalido")