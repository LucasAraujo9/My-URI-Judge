__author__ = 'joaquim'
"""
 URI Online Judge | 1176
Fibonacci em Vetor

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 1

Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que
os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos
os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.
Entrada

A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um
único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.
Saída

Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.
Exemplo de Entrada 	Exemplo de Saída

3
0
4
2

Fib(0) = 0
Fib(4) = 3
Fib(2) = 1
"""
def inputEntradas():
    n = int(input())
    if n > 0 and n > 60:
        return inputEntradas()
    return n

fib = [int(z) for z in range(61)]
cont = 0
antecessor = 0
antecessorAterior = 0
f = 0
num = int(input())
while num > 0:
    n = inputEntradas()
    num -= 1
    if f == 0:
        for i in range(61):
            if cont == 0:
                fib[i] = 0
                antecessorAterior = 0
                cont += 1
            elif cont == 1:
                fib[i] = 1
                antecessor = 1
                cont += 1
            else:
                fib[i] = antecessorAterior + antecessor
                antecessorAterior = antecessor
                antecessor = fib[i]
        f += 1
    print("Fib(%d) = %d" %(n,fib[n]))
    #print("%d - %d]" %(i,fib[i]))
