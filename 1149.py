__author__ = 'joaquim'
"""
 URI Online Judge | 1149
Somando Inteiros Consecutivos

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma dos N números a partir de A(inclusive).
Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.
Entrada

A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.
Saída

A saída contém apenas um valor inteiro.
Exemplo de Entrada 	Exemplo de Saída

    3 2                             7
"""
"""
cont = 0
a = 0
n = 0
lista = []

def entradas():
    global cont
    global a
    global n

    if cont == 0:
        a,n = [int(i) for i in input().split(" ")]
        if n <= 0:
           cont = 2
        if n <= 0:
            return entradas()
    if cont == 2:
        n = int(input())
        if n <= 0:
            return entradas()
    lista.append(a)
    lista.append(n)

def main():
    global a
    global n
    soma = 0
    entradas()
    for i in range(1,n+1):
        soma += a
        a += 1

    print(soma)

if __name__ == "__main__" : main()
"""
cont = 0
a = 0
n = 0
listaEntrada = []
contT = 0
if cont == 0:

    listaEntrada = [int(i) for i in input().split(" ")]
    if listaEntrada[1] <= 0:
        cont = 2
    for i in range(len(listaEntrada)):
        contT += i

    while(cont == 2 ):
        if cont == 2:
            #n = int(input())
            listaEntrada[1] = listaEntrada[contT]
            if listaEntrada[1] > 0:
                break
n = listaEntrada[1]
a = listaEntrada[0]

soma = 0
for i in range(1,n+1):
    soma += a
    a += 1

print(soma)

