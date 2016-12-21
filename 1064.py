__author__ = 'Joaquim Alves'
"""
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar
a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada: A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes número será positivo.

Saída: O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.

7
-5
6
-3.4
4.6
12
4 valores positivos
7.4
"""
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

cont = 0
media = 0
if(n1 > 0):
    cont += 1
    media += n1
if(n2 > 0):
    cont += 1
    media += n2
if(n3 > 0):
    cont += 1
    media += n3
if(n4 > 0):
    cont += 1
    media += n4
if(n5 > 0):
    cont += 1
    media += n5
if(n6 > 0):
    cont += 1
    media += n6

media = media/cont
print("%d valores positivos"%cont)
print(media)