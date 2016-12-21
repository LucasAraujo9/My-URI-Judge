__author__ = 'Joaquim Alves'
"""
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for
possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada: A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y)
que serão lidos em seguida.

Saída: Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso
não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

Exemplo de Entrada	Exemplo de Saída
3
3 -2
-8 0
0 8

-1.5
divisao impossivel
0.0
"""

N = int(input())
lista = []

for i in range(N):
    X,Y = [int(j)for j in input().split(" ")]
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
        if B == 0:
            print("divisao impossivel")
            cont = 0
        elif(A > 0 or B > 0 or A < 0):
            div = A / B
            print("%.1f"%div)
            cont = 0
