__author__ = 'joaquim'
"""
URI Online Judge | 1182
Coluna na Matriz

Por Neilor Tonin, URI Brasil
Timelimit: 1

Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um
caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida,
calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo
ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser considerados
na operação.

Entrada

A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação.
A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média)
que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.
Saída

Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
Exemplo de Entrada 	Exemplo de Saída

5
S
0.0
-3.5
2.5
4.1
...


12.6
###########################CASO DE TESTE QUE EU FIZ##################
1
M
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

26.3

"""
num = int(input())
sm = input()
matriz = []
x = 12

for i in range(x):
    coluna = []
    for j in range(x):
        n = input()
        coluna.append(n)
    matriz.append(coluna[:])

soma = 0.0
media = 0.0

if sm == 'S':
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == num:
                soma += float(matriz[i][j])
    print("%.1f" %soma)

elif sm == 'M':
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == num:
                media += float(matriz[i][j])

    mediaM = media/12
    print("%.1f" %mediaM)

#for i in range (len(matriz)):
#    print(matriz[i])
