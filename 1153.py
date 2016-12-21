__author__ = 'Joaquim Alves'
"""
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N‐1 ) * (N‐2) * (N‐3) * ... * 1 .

Entrada: A entrada contém um valor inteiro N (0 < N < 1 3).
Saída: A saída contém um valor inteiro, correspondente ao fatorial de N.

Exemplo de Entrada              Exemplo de Saída
      4                                24
"""

N = int(input())
i = 1
fatorial = 1
Num = N

while (Num > 1):
    fatorial *= (N - i)
    i += 1
    Num -= 1

print(N*fatorial)