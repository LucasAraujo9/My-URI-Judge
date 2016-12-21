__author__ = 'joaquim'
"""
Resto da Divisão

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Escrever um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele
por 5 for igual a 2 ou igual a 3.
Entrada

O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.
Saída

Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Sample Input 	Sample Output

10                  12
18                    13
                    17


"""

def main():
    X = int(input())
    Y = int(input())

    if X < Y:
        for i in range(X+1, Y):
            if i % 5 == 2 or i % 5 == 3:
                print(i)
    else:
        for i in range(Y+1, X):
            if i % 5 == 2 or i % 5 == 3:
                print(i)

if __name__ == "__main__": main()