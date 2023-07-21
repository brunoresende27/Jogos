from random import randint #Biblioteca usada para números randomicos
from time import sleep #Biblioteca usada para usar um tempo de espera
resultado = randint(0,5)
print('Escolha um número entre 0 e 5 e aguarde o resultado para ver se é o número contemplado ')
num_escolhido = int(input('Digite o número: ')) 
print('Aguarde o resultado...')
sleep(3) #Tempo em segundos
if num_escolhido == resultado:
    print('PARABÉNS!!! Você acertou o número...')
else:
    print('Que pena, você escolheu o número {} e o número correto é {} !'.format(num_escolhido,resultado))
    