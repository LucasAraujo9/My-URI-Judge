__author__ = 'Joaquim Alves'
"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.


Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída
3 2
Total: R$ 10.00
4 3
Total: R$ 6.00
2 3
Total: R$ 13.50
"""

cod,quant = [int(i) for i in input().split(" ")]

if(cod == 1):
    print("Total: R$ %.2f"%(4.0 * quant))
elif(cod == 2):
    print("Total: R$ %.2f"%(4.50 * quant))
elif(cod == 3):
    print("Total: R$ %.2f"%(5.0 * quant))
elif(cod == 4):
    print("Total: R$ %.2f"%(2.0 * quant))
elif(cod == 5):
    print("Total: R$ %.2f"%(1.50 * quant))