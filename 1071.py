__author__ = 'Joaquim Alves'
"""

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada: O arquivo de entrada contém dois valores inteiros.

Saída: O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores
fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada	Exemplo de Saída
6
-5                 5
"""

X = int(input())
Y = int(input())

somaX = 0
somaY = 0

if(X < 0):
    xx = X + 1
    X *= -1
    for i in range(X-1):
        if(xx % 2 > 0):
            somaX += xx
        xx += 1
else:
    xx = X - 1
    for i in range(X-1):
        if(xx % 2 > 0):
            somaX += xx
        xx -= 1
if(Y < 0):
    yy = Y + 1
    Y *= -1
    for j in range(Y-1):
        if(yy % 2 > 0):
            somaY += yy
        yy += 1
else:
    yy = Y - 1
    for j in range(Y-1):
        if(yy % 2 > 0):
            somaY += yy
        yy -= 1

soma = somaX + somaY
print(soma)