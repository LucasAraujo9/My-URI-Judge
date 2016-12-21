__author__ = 'joaquim'
"""
URI Online Judge | 1183
Acima da Diagonal Principal

Por Neilor Tonin, URI Brasil
Timelimit: 1

Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule
e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal principal da matriz,
conforme ilustrado abaixo (área verde).

Entrada

A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que
deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.
Saída

Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.
Exemplo de Entrada 	Exemplo de Saída

S
1.0
0.0
-3.5
2.5
4.1
...
12.6
###########################CASO DE TESTE QUE EU FIZ##################
S
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

1512.0

-------------------------
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

22.9
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
cont = 1
contAux = 11
contGeral = 0
y = 0
if sm == 'S':
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                y += 1
                while(contAux > 0):
                    soma += float(matriz[i][cont])
                    cont += 1
                    contAux -= 1
                if contAux == 0:
                    contAux = 11 - y
                    cont = y + 1
    print("%.1f" %soma)

elif sm == 'M':
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                y += 1
                while(contAux > 0):
            #        print("Cont = %d.....y= %d.......ContAux = %d......: " %(cont,y,contAux))
                    media += float(matriz[i][cont])
                    cont += 1
                    contAux -= 1
                    contGeral += 1
                if contAux == 0:
                    contAux = 11 - y
                    cont = y + 1

    mediaM += media/contGeral

    print("%.1f" %mediaM)

#for i in range (len(matriz)):
#    print(matriz[i])