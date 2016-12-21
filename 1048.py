__author__ = 'Joaquim Alves'
"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

     Salário                    Percentual de Reajuste

     0       - 400.00                  15%
     400.01  - 800.00                  12%
    800.01   - 1200.00                 10%
    1200.01  - 2000.00                  7%
    acima de 2.000                      4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada: A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída: Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
400.00         Novo salario: 460.00
               Reajuste ganho: 60.00
               Em percentual: 15 %

800.01         Novo salario: 880.01
               Reajuste ganho: 80.00
               Em percentual: 10 %
2000.00
Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
"""

salario = float(input())

if(salario > 0 and salario <= 400.00):
    novoSalario = salario+(salario * 0.15)
    reajuste = novoSalario - salario
    print("Novo salario: %.2f"%novoSalario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 15 %")
elif(salario > 400.01 and salario <= 800.00):
    novoSalario = salario+(salario * 0.12)
    reajuste = novoSalario - salario
    print("Novo salario: %.2f"%novoSalario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 12 %")
elif(salario >= 800.01 and salario <= 1200.00):
    novoSalario = salario+(salario * 0.10)
    reajuste = novoSalario - salario
    print("Novo salario: %.2f"%novoSalario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 10 %")
elif(salario >= 1200.01 and salario <= 2000.00):
    novoSalario = salario+(salario * 0.07)
    reajuste = novoSalario - salario
    print("Novo salario: %.2f"%novoSalario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 7 %")
elif(salario > 2000.00):
    novoSalario = salario+(salario * 0.04)
    reajuste = novoSalario - salario
    print("Novo salario: %.2f"%novoSalario)
    print("Reajuste ganho: %.2f"%reajuste)
    print("Em percentual: 4 %")