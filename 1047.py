__author__ = 'Joaquim Alves'
"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada: Quatro números inteiros representando a hora de início e fim do jogo.
Saída: Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

Exemplo de Entrada	Exemplo de Saída
7 8 9 10                   O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
7 7 7 7                    O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)
7 10 8 9                   O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)


###################Testes Avançados#############################
8 9 7 10                   O JOGO DUROU 23 HORA(S) E 1 MINUTO(S)
9 10 7 8                   O JOGO DUROU 21 HORA(S) E 58 MINUTO(S)
"""

hInicio,mInicio,hFim,mFim = [int(i) for i in input().split(" ")]

if(hInicio <= hFim):
    if(mInicio < mFim):
        hFinal = hFim - hInicio
        mFinal = mFim - mInicio
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(hFinal,mFinal))
    else:
        hFinal = (hFim - hInicio)
        if hFinal == 0:
            hFinal = 24
        mFinal = 60 - (mInicio - mFim)
        if mFinal <= 59 and hFinal >= 1:
            hFinal -= 1
        if mFinal == 60:
            mFinal = 0

        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(hFinal,mFinal))

else:
    if(mInicio < mFim):
        hFinal = hInicio - hFim
        hFinal = 24 - hFinal
        mFinal = mFim - mInicio
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(hFinal,mFinal))
    else:
        mFinal = 60 - (mInicio - mFim)
        hFinal = 23 - (hInicio - hFim)
        if hFinal == 0:
            hFinal = 24
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(hFinal,mFinal))
