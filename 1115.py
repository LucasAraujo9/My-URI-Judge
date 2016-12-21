__author__ = 'Joaquim Alves'
"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano.
Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas
coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada: A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.
Saída: Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

Exemplo de Entrada	Exemplo de Saída
2 2
3 -2
-8 -1
-7 1
0 2
primeiro
quarto
terceiro
segundo
"""

a = 1
lista = []
while(a > 0):
    X,Y = [int(i) for i in input().split(" ")]
    if X == 0:
        break
    if Y == 0:
        break
    lista.append(X)
    lista.append(Y)

cont = 0

for i in range(len(lista)):
    if cont == 0:
        A = lista[i]
    if cont == 1:
        B = lista[i]
    cont += 1
    if cont == 2:
        if A > 0 and B > 0:
            print("primeiro")
            cont = 0
        if A > 0 and B < 0:
            print("quarto")
            cont = 0
        if A < 0 and B < 0:
            print("terceiro")
            cont = 0
        if A < 0 and B > 0:
            print("segundo")
            cont = 0