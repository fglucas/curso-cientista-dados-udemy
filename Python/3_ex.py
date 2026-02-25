# Crie um programa que leia o peso de uma carga em números inteiros.
# Se o peso for até 10kg, informe que o valor será de R$50,00.
# Entre 11 e 20Kg será de R$80,00
# Se for maior que 20 o transporte não é aceito.

while True:
    try:
        peso = float(input("Digite o valor da carga deseja: "))
        if peso <= 10.0:
            print(f"Peso informado {peso}, valor da faixa de peso: R$50,00")
            break
        elif peso >= 10.1 and peso <= 20:
            print(f"Peso informado {peso}, valor da faixa de peso: R$80,00")
            break
        else:
            print(f"Peso informado {peso}, maior que o limite de 20kg. Transporte não aceito" )
            break
    except:
        print("Tente novamente")
