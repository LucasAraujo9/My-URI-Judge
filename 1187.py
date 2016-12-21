__author__ = 'joaquim'
"""
 URI Online Judge | 1187
Área Superior

Por Neilor Tonin, URI Brasil
Timelimit: 1

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida,
calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área superior da matriz,
conforme ilustrado abaixo (área verde).

Entrada

A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média)
que deverá ser realizada com os elementos da matriz. Seguem 144 valores com ponto flutuante de dupla precisão que
compõem a matriz.
Saída

Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
Exemplo de Entrada 	Exemplo de Saída

S
1.0
330.0
-3.5
2.5
4.1
...


112.4
"""
sm = input()
matriz = []
x = 12
mediaM = 0

for i in range(x):
    coluna = []
    for j in range(x):
        n = input()
        coluna.append(n)
    matriz.append(coluna[:])

soma = 0.0
media = 0.0
cont = 11
contAux = 0
contGeral = 0
contMatriz = 11
y = 0
q = 10
if sm == 'S':
    for i in range(len(matriz)-11):
        y += 1
        for j in range(len(matriz)):
            while contAux < q:
                print(i,j)
                soma += float(matriz[i+1][j+1])
                contAux += 1
            q -= 1
            contAux = 0

    print("%.1f" %soma)

elif sm == 'M':
    for i in range(len(matriz)):
        y += 1
        for j in range(len(matriz)):
            while(contAux > 0 ):
                media += float(matriz[i][cont])
                cont -= 1
                contAux -= 1
                contGeral += 1
        if contAux == 0:
            contAux = y
            cont = 11

    mediaM += media/contGeral

    print("%.1f" %mediaM)

#for i in range (len(matriz)):
#    print(matriz[i])