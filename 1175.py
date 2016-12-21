__author__ = 'joaquim'
"""
 URI Online Judge | 1175
Troca em Vetor I

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o
penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.
Entrada

A entrada contém 20 valores inteiros, positivos ou negativos.
Saída

Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.
Exemplo de Entrada 	Exemplo de Saída

0
-5
...
63
230

N[0] = 230
N[1] = 63
...
N[18] = -5
N[19] = 0
"""
n = [int(i) for i in range(20)]

for i in range(20):
    num = int(input())
    n[i] = num

aux = 0
cont = 19

for i in range(10):
    aux = n[i]
    n[i] = n[cont]
    n[cont] = aux

    cont -= 1

for j in range(len(n)):
    print("N[%d] = %d" %(j,n[j]))

