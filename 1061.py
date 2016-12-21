__author__ = 'Joaquim Alves'
"""
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando
dentro do mês. O problema é que Pedrinho quer calcular o tempo em segundos que o evento vai durar, uma vez que ele sabe
quando inicia e quando termina o evento..
Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada: Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída: Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplos de Entrada	Exemplos de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23        3 dia(s)
                    22 hora(s)
                    1 minuto(s)
                    0 segundo(s)
Dia 5
08 : 12 : 23
Dia 6
08 : 12 : 24
                    1 dia(s)
                    0 hora(s)
                    0 minuto(s)
                    1 segundo(s)

####################Extras Cases Tests#######################
Dia 9
06 : 13 : 23
Dia 5
08 : 12 : 23

-3 dia(s)
-22 hora(s)
-1 minuto(s)
0 segundo(s)
------------------------------------------------------------
Dia 9
06 : 13 : 23
Dia 9
08 : 12 : 23
Saida Esperada
0 dia(s)
1 hora(s)
59 minuto(s)
0 segundo(s)
Minha Saida Errada
0 dia(s)
0 hora(s)
1 minuto(s)
0 segundo(s)
###################################################
Dia 9
06 : 13 : 50
Dia 9
08 : 12 : 23
0 dia(s)
1 hora(s)
58 minuto(s)
33 segundo(s)
##############################################################
Dia 1
4 : 5 : 6
Dia 2
1 : 2 : 3
-------------------------0 dia(s)
-------------------------20 hora(s)
-------------------------56 minuto(s)
-------------------------57 segundo(s)
##############################################################3
Dia 23
12 : 00 : 00
Dia 30
12 : 00 : 00
-------------------------7 dia(s)
-------------------------0 hora(s)
-------------------------0 minuto(s)
-------------------------0 segundo(s)
"""

diaString, dia1 = input().split(" ")
dia1 = int(dia1)

hh, mm, ss = [int(i) for i in input().split(" : ")]

diaString2,dia2 = input().split(" ")
dia2 = int(dia2)

hh2, mm2, ss2 = [int(i) for i in input().split(" : ")]

data1 = 0
data2 = 0

data1 = (dia1 * 86400) + (hh * 3600) + (60 * mm) + ss
data2 = (dia2 * 86400) + (hh2 * 3600) + (60 * mm2) + ss2


dataFinal = 0
dataFinal = data2 - data1
data = 0
data = dataFinal / 86400        #Ok
horaFinal = 0

horaFinal = (dataFinal%86400)/3600
minFinal = 0
minFinal = ((dataFinal%86400)%3600)/60
segFinal = 0
segFinal = ((dataFinal%86400)%3600)%60

print("%d dia(s)"%data)
print("%d hora(s)"%horaFinal)
print("%d minuto(s)"%minFinal)
print("%d segundo(s)"%segFinal)