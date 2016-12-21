__author__ = 'Joaquim Alves'
"""
Neste problema você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda
para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

Entrada: A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída: Imprima o nome do animal correspondente à entrada fornecida.

Exemplos de Entrada	Exemplos de Saída
vertebrado
mamifero
onivoro             homem

vertebrado
ave
carnivoro           aguia

invertebrado
anelideo
onivoro              minhoca

"""
tipo1 = input()
tipo2 = input()
tipo3 = input()

if(tipo1 == 'vertebrado'):
    if(tipo2 == 'ave'):
        if(tipo3 == 'carnivoro'):
            print("aguia")
        else:
            print("pomba")
if(tipo1 == 'vertebrado'):
    if(tipo2 == 'mamifero'):
        if(tipo3 == 'onivoro'):
            print("homem")
        else:
            print("vaca")
if(tipo1 == 'invertebrado'):
    if(tipo2 == 'inseto'):
        if(tipo3 == 'hematofago'):
            print("pulga")
        else:
            print("lagarta")
if(tipo1 == 'invertebrado'):
    if(tipo2 == 'anelideo'):
        if(tipo3 == 'hematofago'):
            print("sanguessuga")
        else:
            print("minhoca")