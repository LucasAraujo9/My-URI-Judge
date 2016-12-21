__author__ = 'joaquim'
"""
 URI Online Judge | 1158
Soma de Ímpares Consecutivos III

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois
inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar.
Por exemplo:
para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13
Entrada

A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.
Saída

Imprima a soma dos consecutivos números ímpares a partir do valor X.
Exemplo de Entrada 	Exemplo de Saída

2
4 3
11 2

21
24
"""

listaNumeros = []

n = int(input())

while n > 0:
    x, y = [int(i) for i in input().split(" ")]
    listaNumeros.append(x)
    listaNumeros.append(y)
    n -= 1

cont = 1
soma = 0
z = 0
k = 0
for i in listaNumeros:
    if cont == 1:
        z = i
    if cont == 2:
        k = i
        for j in range(k):
            if z % 2 == 0:
                z += 1
            if z % 2 > 0:
                soma += z
                z += 2
            #print(soma)
        cont = 0
        print(soma)

        soma = 0
    cont += 1
