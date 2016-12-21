__author__ = 'joaquim'

"""
 URI Online Judge | 1145
Sequência Lógica 2

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.
Entrada

O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).
Saída

Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.
Exemplo de Entrada 	Exemplo de Saída

3 99

1 2 3
4 5 6
7 8 9
10 11 12
...
97 98 99

"""

x, y = [int(i) for i in input().split(" ")]

cont = x
lista = []

def exibeLista(List, Char):
    return str(Char).join([str(i) for i in List])

for i in range(1, y + 2):
    if cont == 0:
        print(exibeLista(lista," "))
        lista = []
        cont = x
    if cont >= 1:
        lista.append(i)
        cont -= 1