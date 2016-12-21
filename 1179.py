__author__ = 'joaquim'
"""
URI Online Judge | 1179
Preenchimento de Vetor IV

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares.
Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher,
você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a
leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor
impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.
Entrada

A entrada contém 15 números inteiros.
Saída

Imprima a saída conforme o exemplo abaixo.
Exemplo de Entrada 	Exemplo de Saída

1
3
4
-4
2
3
8
2
5
-7
54
76
789
23
98

par[0] = 4
par[1] = -4
par[2] = 2
par[3] = 8
par[4] = 2
impar[0] = 1
impar[1] = 3
impar[2] = 3
impar[3] = 5
impar[4] = -7
impar[0] = 789
impar[1] = 23
par[0] = 54
par[1] = 76
par[2] = 98
"""

impar = [int(i) for i in range(5)]
par = [int(i) for i in range(5)]
listaImpar = []
listaPar = []
contPar = 0
contImpar = 0

for i in range(15):
    num = int(input())
    if num % 2 == 0:
        #par[contPar] = num
        listaPar.append(num)
        contPar += 1
    else:
        #impar[contImpar] = num
        listaImpar.append(num)
        contImpar += 1

    if contImpar == 5:
        for i in range(5):
            print("impar[%d] = %d" %(i,listaImpar[i]))
        contImpar = 0
        #impar = [int(i) for i in range(5)]
        listaImpar = []

    if contPar == 5:
        for i in range(5):
            print("par[%d] = %d" %(i,listaPar[i]))
        contPar = 0
        listaPar = []
        #par = [int(i) for i in range(5)]



if contImpar > 0:
    for i in range(len(listaImpar)):

        print("impar[%d] = %d" %(i,listaImpar[i]))

if contPar > 0:
    for i in range(len(listaPar)):
        print("par[%d] = %d" %(i,listaPar[i]))
