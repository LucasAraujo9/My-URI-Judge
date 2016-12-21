__author__ = 'Joaquim Alves'
"""
A seguinte sequência de números 0 1 1 2 3 5 8 1 3 21 ... é conhecida como série de Fibonacci. Nessa
sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo
que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.
Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).
Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver
espaço após o último valor.

Exemplo de Entrada           Exemplo de Saída
5                               0 1 1 2 3

#9
#0 1 1 2 3 5 8 13 21
#0 1 2 3 4 5 6  7  8
"""

listaFib = []

def inputEntradas():
    n = int(input())
    if n > 0 and n > 46:
        return inputEntradas()
    return n

def funcFibonacci():
    cont = 0
    x = inputEntradas()
    if x < 46:
        i = x
    anterior = 0

    for y in range(i):
        if cont == 0:
            #print(y)
            anterior = y
            cont += 1
            listaFib.append(y)
        elif cont == 1:
            y += anterior
            #print(y)
            anterior = y
            cont += 1
            listaFib.append(y)
        elif cont == 2:
            y = 1
            #print(y)
            antecessorAnterior = y
            cont += 1
            listaFib.append(y)
        elif cont == 3:
            y = anterior + antecessorAnterior
            #print(y)
            antecessorAnterior = anterior
            anterior = y
            listaFib.append(y)

def exibeLista(List, Char):
    return str(Char).join([str(item) for item in List])

def main():
    funcFibonacci()
    print(exibeLista(listaFib," "))

if __name__ == "__main__" : main()
