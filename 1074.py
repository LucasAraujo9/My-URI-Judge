__author__ = 'Joaquim Alves'
"""
Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido,
mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou
negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL),
pois por definição zero é par, seu programa deverá imprimir apenas NULL.

Entrada: A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste.
caso de teste a seguir é um valor inteiro X (-107 < X <107).

Saída: Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão
ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

Exemplo de Entrada	Exemplo de Saída
4
-5
0
3
-4
ODD NEGATIVE
NULL
ODD POSITIVE
EVEN NEGATIVE
"""

N = int(input())
valor = []

for i in range(N):
    v = int(input())
    valor = valor + [v]

for i in range(len(valor)):
    if(valor[i] == 0):
        print("NULL")
    elif(valor[i] % 2 == 0 and valor[i] < 0):
        print("EVEN NEGATIVE")
    elif(valor[i] % 2 == 0 and valor[i] > 0):
        print("EVEN POSITIVE")
    elif(valor[i] % 2 > 0 and valor[i] > 0):
        print("ODD POSITIVE")
    else:
        print("ODD NEGATIVE")
"""
ODD NEGATIVE
NULL
ODD POSITIVE
EVEN NEGATIVE"""