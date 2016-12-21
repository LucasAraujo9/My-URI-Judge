__author__ = 'Joaquim Alves'
"""
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele
não existem políticos corruptos e os recursos arrecadados são utilizados em benefício da população, sem qualquer desvio.
A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o
valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.

Lembre que, se o salário for R$ 3000.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário
que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8%
sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada: A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
Saída: Imprima o texto "R$" seguido de um espaço e do valor total devido de Imposto de Renda, com duas casas após o ponto.
Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem "Isento".

Exemplos de Entrada	Exemplos de Saída
3002.00               R$ 80.36
1701.12               Isento
4520.00              R$ 355.60
"""

salario = float(input())

if(salario >= 0.00 and salario <= 2000.00):
    print("Isento")

if(salario >= 2000.01 and salario <= 3000.00):
    imposto = (salario - 2000.00) * 0.08
    print("R$ %.2f"%imposto)
if(salario >= 3000.01 and salario <= 4500.00):
    imposto1 = salario - 3000
    impostoAnterior = salario - 2000.00
    impostoAnterior -= imposto1
    impostoAnterior *= 0.08
    imposto1 *= 0.18
    imposto = imposto1 + impostoAnterior
    print("R$ %.2f"%imposto)
if(salario > 4500.00):
    imposto1 = salario - 4500.00
    impostoAnterior = salario - 3000.00
    impostoAnterior -= imposto1
    impostoAnterior2 = salario - 2000.00
    impostoAnterior2 = impostoAnterior2 - impostoAnterior - imposto1
    imposto1 *= 0.28
    impostoAnterior *= 0.18
    impostoAnterior2 *= 0.08
    imposto = imposto1 + impostoAnterior + impostoAnterior2
    print("R$ %.2f"%imposto)

    """
    teste = salario - 2000
    print(teste)
    impost11 = (salario - 3000.00)
    print(impost11)
    imposto1 = (salario - 2000.00) * 0.08
    imposto2 = (salario - 3000.00) * 0.18
    imposto = imposto1 + imposto2
    print("R$ %.2f"%imposto)
6235.35
2765.41
4100.00
672.00

output correto:
CÓDIGO: SELECIONAR TODOS
R$ 835.90
R$ 61.23
R$ 278.00
Isento

"""