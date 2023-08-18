from turtle import Turtle
from time import sleep
t = Turtle()# Inicializar
t.speed(1)#Velocidade
def receber_distancia():
    if direcao in 'Tt':
        resposta = distancia = int(input('Distância: '))
        t.backward(distancia)
        return resposta
        
    else:
        resposta = distancia = int(input('Distância: '))
        t.forward(distancia)
        return resposta
def receber_angulo():
    angulo = int(input('Ângulo: '))
    t.right(angulo)
    return angulo

while True:
    print('=-=-ESCOLHA A DIREÇÃO=-=-')
    direcao = str(input('\033[1;32m[F] - FRENTE\n[T] - TRÁZ\n[D] - DIREITA\n[E] - ESQUERDA\033[m\n\033[1;31m[X] - SAIR DO PROGRAMA\033[m\n')).strip()[0]
    if direcao in 'Ff':
        distancia = receber_distancia()
    elif direcao in 'Tt':
        distancia = receber_distancia()
        t.backward(distancia)
    elif direcao in 'Dd':
        angulo = receber_angulo()
        distancia = receber_distancia()
    elif direcao in 'Ee':
        angulo = receber_angulo()
        distancia = receber_distancia()
    elif direcao in 'Xx':
        print('Obrigado por jogar, Até a proxima!')
        break
    else:
        print('\033[1;31mFavor digitar um dado valido!\033[m')
        sleep(2)
print('-='*10)
    

    