__author__ = 'Joaquim Alves'
"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada: O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai
conter um número nulo ou negativo.

Saída: Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2
6 3
5 0
2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""

lista = []
a = 1
listaSoma = []

while (a != 0):
    M, N = [int(i) for i in input().split(" ")]
    if M == 0:
        N = 0
        break
    if N == 0:
        M = 0
        break
    if M < 0:
        break
    if N < 0:
        break
    lista.append(M)
    lista.append(N)

def rp_ListItemsToString(List, Char):
    return str(Char).join([str(item) for item in List])

listaAux = []

cont = 0
A = B = 0
somaNumListas = 0

for i in range(len(lista)):
    if cont == 0:
        A = lista[i]
    if cont == 1:
        B = lista[i]
    cont += 1

    if cont == 2:
        if A > B:
            for j in range(B,A+1):
                listaAux.append(j)
                somaNumListas += j
            print(rp_ListItemsToString(listaAux,' '),"Sum=%d"%somaNumListas)
            cont = 0
            listaAux = []
            somaNumListas = 0
        else:
            for j in range(A,B+1):
                listaAux.append(j)
                somaNumListas += j
            print(rp_ListItemsToString(listaAux,' '),"Sum=%d"%somaNumListas)
            cont = 0
            listaAux = []
            somaNumListas = 0