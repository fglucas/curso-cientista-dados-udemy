# 1 - Faça um programa que tenha uma função chamada amplitude. A função deve receber uma lista e imprimir a amplitude.
#     Crie também um código para testar a sua função.


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


lista_numeros = []

while True:
    entrada = input("Digite um número (ou qualquer outra coisa para sair): ")

    if is_number(entrada):
        lista_numeros.append(float(entrada))
    else:
        print("Entrada inválida. Finalizando...")
        break

print("Números inseridos:", lista_numeros)

def amplitude(lista_numeros):
    return max(lista_numeros) - min(lista_numeros)
x = amplitude(lista_numeros)

print(f"A amplitude da lista é: {x}")