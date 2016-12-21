__author__ = 'joaquim'
"""
 URI Online Judge | 1165
Número Primo

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número
7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.
Entrada

A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número
 de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107),
 que pode ser ou não, um número primo.
Saída

Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação
fornecida.
Exemplo de Entrada 	Exemplo de Saída

3
8
51
7

8 nao eh primo
51 nao eh primo
7 eh primo
"""
cont = 0
entradas = int(input())

while(entradas > 0):
    num = int(input())

    for i in range(1,num+1):
        if num % i == 0:
            cont += 1


    if num == 0 or num == 1:
        print("%d nao eh primo" %num)
        cont = num = 0
    elif cont > 2:
        print("%d nao eh primo" %num)
        cont = num = 0
    else:
        print("%d eh primo" %num)
        cont = num = 0

    entradas -= 1