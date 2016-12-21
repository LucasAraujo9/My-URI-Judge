__author__ = 'Joaquim Alves'
"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule
o perímetro do triângulo e apresente a mensagem:
Perimetro = XX. X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a
mensagem
Area = XX. X
Entrada
A entrada contém três valores reais.
Saída
O resultado deve ser apresentado com uma casa decimal.
Exemplo de Entrada Exemplo de Saída
6. 0 4. 0 2. 0 Area = 10. 0
6. 0 4. 0 2. 1 Perimetro = 12. 1
"""

A,B,C = [float(i) for i in input().split(" ")]

if A + B > C and A + C > B and B + C > A:
    perimetro = A + B + C
    print("Perimetro = %.1f"%perimetro)
else:
    area = ((A + B)*C)/2
    print("Area = %.1f"%area)