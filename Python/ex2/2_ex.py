# Faça uma função que receba uma string e imprima esta string na forma vertical
# se receber PYTHON deve imprimi-lo em na vertical.

def vertical(texto):
    """Imprime cada caractere da string em uma linha vertical."""
    for caractere in texto:
        print(caractere)

# Exemplo de uso:
palavra = input("Digite uma palavra: ")
vertical(palavra)