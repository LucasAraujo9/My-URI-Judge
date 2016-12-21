__author__ = 'joaquim'
"""
 URI Online Judge | 1146
Sequências Crescentes

Adaptado por Neilor Tonin, URI Brasil
Timelimit: 2

Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.

Obs: cuide para não deixar espaço em branco após o último valor apresentado na linha ou você receberá Presentation Error.
Entrada

O arquivo de entrada contém vários números inteiros. O último número no arquivo de entrada é 0.
Saída

Para cada número N do arquivo de entrada deve ser impressa uma linha de 1 até N, conforme o exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.
Exemplo de Entrada 	Exemplo de Saída

5
10
3
0
1 2 3 4 5
1 2 3 4 5 6 7 8 9 10
1 2 3
"""
lista = []
listaSaida = []

def entradas():
    n = int(input())
    while n != 0:
        if n > 0:
            lista.append(n)
        else:
            return 0
        n = int(input())


def saida():
    for i in lista:
        listaSaida = []
        for j in range(1,i+1):
            listaSaida.append(j)
        print(exibeLista(listaSaida," "))


def exibeLista(List, Char):
    return str(Char).join([str(item) for item in List])

def main():
    entradas()
    saida()

if __name__ == "__main__": main()