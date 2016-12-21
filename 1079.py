__author__ = 'Joaquim Alves'
"""
Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste
de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos
de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

Entrada: O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

Saída: Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
3
6.5 4.3 6.2
5.1 4.2 8.1
8.0 9.0 10.0
5.7
6.3
9.3
"""

N = int(input())
lista2 = []
cont = 0
n1 = n2 = n3 = 0
m = 0

for i in range(N):
    lista = [float(i) for i in input().split(" ")]
    lista2.append(lista)

for i in range(len(lista2)):
    if(cont == 0):
        n1 = lista2[i][0]
        n2 = lista2[i][1]
        n3 = lista2[i][-1]
        cont += 1
    if(cont == 1 ):
        m = ((n1 * 2) + (n2 * 3) + (n3 * 5))/10
        print("%.1f"%m)
        n1 = n2 = n3 = m = 0.0
        cont = 0
