p=input('Poderia responder algumas perguntas?')
p1=float(input('Qual o seu peso?'))
p2=float(input('Qual a sua altura?'))
p3=int(input('Quantos anos voçê tem?'))
print('Então você pesa {} kilos tem {} de altura e tem {} anos,correto?'.format(p1, p2, p3 ))
p4=input('Sim ou não?')
print('Muito obrigado pela compreensão!')
---------------------------------------------------------------------------------------------------
# exercicios

#005 
d=int(input('Digite um número:'))
an=d-1
su=d+1
print('O seu antecessor e {}, o sucessor é {}'.format(an,su))

#006
n=int(input('digite um número:'))
do=n*2
tri=n*3
r=n**(1/2)
print('O dobro será {},o triplo será {} e raiz quadrada de {}'.format(do,tri,r))

#007
n=int(input('digite um número:'))
do=n*2
tri=n*3
r=n**(1/2)
print('O dobro será {},o triplo será {} e raiz quadrada de {}'.format(do,tri,r))

#008
v=float(input('Digite um valor em metro:'))
c1=float(v*100)
c2=float(v*1000)
print('A coversão em cm é {},em mm é {}'.format(c1,c2))

009
n=int(input('Digite o número que voçê queira saber a tabuada:'))
t1=n*1
t2=n*2
t3=n*3
t4=n*4
t5=n*5
t6=n*6
t7=n*7
t8=n*8
t9=n*9
t10=n*10
print('a tabuada do {} fica assim:'.format(n))
print('{} X 1 = {}'.format(n,t1))
print('{} X 2 = {}'.format(n,t2))
print('{} X 3 = {}'.format(n,t3))
print('{} X 4 = {}'.format(n,t4))
print('{} X 5 = {}'.format(n,t5))
print('{} X 6 = {}'.format(n,t6))
print('{} X 7 = {}'.format(n,t7))
print('{} X 8 = {}'.format(n,t8))
print('{} X 9 = {}'.format(n,t9))
print('{} X 10 = {}'.format(n,t10))

010
d=float(input('quanto você tem em dinheiro em sua carteira: R$'))
dl=d/4.90
print('Com {} reais você pode comprar {:.2f} dólares'.format(d,dl))

011
l=float(input('Digite a largura:'))
Al=float(input('Digite a altura:'))
area=int(l*Al)
tinta=int(area/2)
print('a area total é {},necessita {} litros de tinta'.format(area,tinta))

012
p=float(input('Digite o preço:'))
nv=int(p-(p*0.05))
print('O preço com desconto fica {} reais'.format(nv))

013
sal=float(input('Digite o seu salário:'))
aum=int(sal+(sal*0.15))
print('O salário com aumento de 15% fica {} reais'.format(aum))
------------------------------------------------------------------
016
from math import trunc
num=float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

017

018
import math
an=float(input('Digite o ângulo que você deseja:'))
sen=math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, sen))
cos= math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan= math.tan(math.radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))
 
 #OU MAIS SIMPLES
 
 from math import radians,sin, cos, tan
an=float(input('Digite o ângulo que você deseja:'))
sen=sin(radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, sen))
cose=cos(radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cose))
tan=tan(radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))

019
import random
n1=input('primeiro nome: ')
n2=input('segundo nome: ')
n3=input('terceiro nome: ')
n4=input('quarto nome: ')
lista=[n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#OU

from random import choice
n1=input('primeiro nome: ')
n2=input('segundo nome: ')
n3=input('terceiro nome: ')
n4=input('quarto nome: ')
lista=[n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

020
import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

#OU

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))   

022

nome = str(input('Digite seu nome:')).strip()            
print('O nome com letras maiúsculas fica: {}'.format(nome.upper()))
print('O nome com letras minúsculas fica: {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

023
num = int(input('digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('O valor da unidade é: {}'.format(u))
print('O valor da dezena é: {}'.format(d))
print('O valor da centena é: {}'.format(c))
print('O valor do milhar é: {}'.format(m))

024
cid = str(input('Digite o nome da cidade:')).strip()
print(cid[:5].upper() == 'SANTO')

025
nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
026
frase = str(input('digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra a apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

027
n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em te conhecer {}!'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

028
from random import randint
computador = randint(0, 5)
print('-=*20')
print('Vou pensar em número entre 0 e 5. Tente adivinhar....')
print('-=*20')
jogador = int(input('Qual número eu pensei? '))
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print('Eu ganhei em pensei no número {} e não no {}!'.format(computador, jogador))
    #OU
print('Vamos brincar?! Vou escolher um número de 0 a 5')
print('Já pensei...Agora Adivinhe!')
adivinhe = int(input('Qual é o número? '))
print('Você acertou!' if adivinhe == 2 else'Não foi dessa vez,tente novamente!')

029

velocidade = int(input('Verificamos e a velocidade do carro foi:'))
multa = (velocidade - 80) * 7.0
if velocidade > 80:
    print('Você foi multado!')
    print('O valor da multa é de R${:.2f}'.format(multa))
else:
    print('Muito bem!Você está dentro do limite de velocidade')

030

num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print('esse número {} é PAR'.format(num))
else:
    print('Esse número {} é ÍMPAR'.format(num))


031

dis = float(input('Qual é a distancia da sua viagem? '))
if dis <= 200:
    preço = dis * 0.50
    print('Sua viagem e menor que 200 KM')
else:
    preço = dis * 0.45
    print('Sua viagem e maior que 200 KM,você terá desconto!')
print('O valor da viagem será de R${:.2f}'.format(preço))

032
from datetime import date
ano = int(input('Digite um ano que queira analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não e BISSEXTO'.format(ano))

033
a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))

034
sal = float(input('Qual o valor do seu salário: '))
if sal <= 1250:
    aumento = sal + (sal * 15/ 100)
else:
    aumento = sal + (sal * 10/ 100)
print('O seu salário com aumento fica R${:.2f}'.format(aumento))

035
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')

036

valor_casa = float(input('Qual o valor da casa que deseja comprar? '))
valor_salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos deseja pagar? '))

parcelas = valor_casa / (anos * 12)
excedencia = valor_salario * 0.7 # ou 30 / 100

if parcelas <= excedencia:
    print('Com o salário de {:.2f},você conseguirá pagar a casa!'.format(valor_salario))
    print('\033[32mEmpréstimo APROVADO!')
else:
    print('Com atual salário de {:.2f}, não será o suficente para pagar a casa em {} anos'.format(valor_salario,anos))
    print('\033[31mEmpréstimo NEGADO!')
print('\033[1;34mObrigado pela preferência!\033[m')

037

num = int(input('Digite um número inteiro:'))
print('pretendo converter {} em qual base?'.format(num))
print('''      
                ESCOLHA
      
      [ 1 ] converter em binário 
      [ 2 ] converter em octal 
      [ 3 ] converter em hexadecimal''')

opção = int(input('Digite sua opção:'))
if opção == 1:
    print('A conversão de {} para binário fica {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('A conversão de {} para octal fica {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('A conversão de {} para hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpção inválida')

038
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
maior = n2
if n2 < n1:
    maior = n1
    print('O primeiro valor é maior,sendo o número {}'.format(maior))
elif n1 < n2:
    maior = n2
    print('O segundo valor é maior,sendo o número {}'.format(maior))
elif n1 == n2:
    print('Não existe valor maior,os dois são iguais!')

039

from datetime import date
nasc = int(input('Digite o ano que você nasceu:'))
data = date.today().year
idade = data - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, data))
if idade < 18:
    prazo = 18 - idade
    ano = data + prazo
    print('Não é hora ainda,você irá se alistar ainda falta {} ano, seu alistamento será em {}'.format(prazo, ano))
elif idade == 18:
    print('Já é hora de se alistar!')
elif idade > 18:
    prazo = idade - 18
    ano = data - prazo
    print('Já passou da hora de se alistar,Você passou {} ano do prazo de alistamento,seu alistamento foi em {}'.format(prazo,ano))
  

040

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
média =(n1 + n2 )/2

if média < 5.0:
    print('Sua nota foi abaixo da média da escola,você está \033[1;31mREPROVADO!')
elif média >= 5.0 and média <= 6.9:
    print('Você está de \033[1;31mRECUPERAÇÃO!')
elif média >= 7.0 and média <= 10:
    print('Parabéns você foi \033[1;32mAPROVADO!')
elif média >= 10.1:
    print('\033[1;31mErro :/\033[m')
    print('Digite sua nota de 0 a 10,por favor!')

041

from datetime import date
nasc = int(input('Digite sua data de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Sua categoria é MIRIM de acordo com sua idade de {} anos'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL de acordo com sua idade de {} anos'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua categoria é JUNIOR de acordo com sua idade de {} anos'.format(idade))
elif idade > 19 and idade <= 20:
    print('Sua categoria é SÊNIOR de acordo com sua idade de {} anos'.format(idade))
elif idade > 20:
    print('Sua categoria é MASTER de acordo com sua idade de {} anos'.format(idade))

#OU
    
from datetime import date
nasc = int(input('Digite sua data de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Sua categoria é MIRIM de acordo com sua idade de {} anos'.format(idade))
elif idade <= 14:
    print('Sua categoria é INFANTIL de acordo com sua idade de {} anos'.format(idade))
elif idade <= 19:
    print('Sua categoria é JUNIOR de acordo com sua idade de {} anos'.format(idade))
elif idade <= 20:
    print('Sua categoria é SÊNIOR de acordo com sua idade de {} anos'.format(idade))
elif idade > 20:
    print('Sua categoria é MASTER de acordo com sua idade de {} anos'.format(idade))


042

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulo ', end ='')
    if  r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar triângulo!')

043

peso = float(input('Quanto você pesa? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso, tente comer mais!!')
elif imc >= 18.5 and imc <= 25:
    print('Você está com o peso ideal')
elif imc >= 25 and imc <= 30:
    print('Cuidado você sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Procure fazer uma atividade física,você está obeso(a)!')
elif imc > 40:
    print('Procure um médico! você está com obesidade mórbida')

    #OU
    peso = float(input('Quanto você pesa? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está abaixo do peso, tente comer mais!!')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal')
elif  25 <= imc < 30:
    print('Cuidado você sobrepeso')
elif  30 <= imc < 40:
    print('Procure fazer uma atividade física,você está obeso(a)!')
elif imc >= 40:
    print('Procure um médico! você está com obesidade mórbida')

044

valor_produto = float(input('Digite o valor do produto: R$'))
print('Agora escolha o método de pagamento')
print('''
      [1] á vista no dinheiro com 10% de desconto
      [2] á vista no cartão com 5% de desconto
      [3] Em 2x no cartão sem juros
      [4] Em 3x ou mais no cartão com 20% de juros''')
opção = int(input('Selecione o método de pagamento: '))

if opção == 1:
    valor = valor_produto * 0.9
    print(' Á vista no dinheiro o valor ficou {:.2f}'.format(valor))
elif opção == 2:
    valor = valor_produto * 0.95
    print('Á vista no cartão o valor ficou {:.2f}'.format(valor))
elif opção == 3:
    valor = valor_produto / 2
    print('O valor dividido em 2x no cartão ficou R${:.2f} sendo o valor total de R${:.2f}'.format(valor,valor_produto))
elif opção == 4:
    valor = valor_produto + (valor_produto * 0.2)
    totparc = int(input('Quantas parcelas? '))
    parcelas = valor / totparc
    print('O valor total do produto dividido em {}x no cartão fica R${:.2f},sendo o valor de cada parcela de R${:.2f}'.format(totparc, valor, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor_produto, valor))
else:
    total = 0
    print('\033[;31mOPÇÃO INVÁLIDA DE PAGAMENTO!')

045

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
        
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
       print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('\033[1;31mJOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!')

046
from time import sleep
print('CONTAGEM REGRESSIVA PARA OS FOGOS')
for c in range(10, -1, -1 ):
    print(c)
    sleep(1)
print('\033[1;31mFogos!!!!')

047
for n in  range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('ACABOU')

#OU

for n in  range(2, 51, 2):
    print(n, end=' ')
print('ACABOU')

048
for imp in range(1, 501):
    if imp % 2 != 0 and imp % 3 == 0:
        print(imp, end= ' ')

049
n=int(input('Digite o número que voçê queira saber a tabuada:'))
print('\033[1;36mA TABUADA DO {}\033[m'.format(n))
print('--'*6)
for num in range(0,11):
    print('{} X {} = {}'.format(n,num,n*num))
print('--'*6)

050
s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        s += num
        cont += 1
print('São {} pares e a soma foi {}'.format(cont, s))

051
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m',end= ' ')
        tot += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end=' ')
print('\033[mo número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')

053
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

    #OU

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

054
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

055
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))

056
médiaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('---- {}ª PESSOA ----'.format(pessoa))
    n = str(input('Nome:')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]:')).strip()
    somaidade += i
    if pessoa == 1 and s in 'Mm':
        maioridadehomem = i
        nomevelho = n
    if s in 'Mm' and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n
    if s in 'Ff' and i > 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

057
sexo =  str(input('Qual o seu sexo? [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('DADOS INVÁLIDOS, digite novamente seu sexo [M/F]: '))
print('O seu sexo é {}'.format(sexo))

#MINHA VERSÃO---------------------------------------------------------
sexo = str((input('Qual o seu sexo? [M/F]: '))).upper().strip()[0]

while sexo not in 'MmFf':
    print('\033[1;31mErro! Digite novamente!\033[m')
    sexo = str(input('Qual o seu sexo? [M/F]')).upper()

if sexo == 'M':
    print('\033[1;34mO seu sexo e Masculino!\033[m')

elif sexo == 'F':
    print('\033[1;35mO seu sexo e Feminimo\033[m')
#----------------------------------------------------------------------

058

from random import randint
computador = randint(0, 10)
print('-=' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar....')
print('-=' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente de novo')
        elif jogador > computador:
            print('Menos... Tente de novo')
print('Acertou com {} tentativas'.format(palpites))

# MINHA VERSÃO]
import time
from random import randint

print('=-'*20)
print('BEM VINDO AO JOGO DA ADIVIAÇÃO DE NÚMEROS')
print('=-'*20)

print('VOU PENSAR EM UM NÚMERO DE 0 A 10, TENTE ADIVINHAR')
print('PENSANDO...')
time.sleep(1.5)
print('HMM...')
time.sleep(1.3)
print('PENSEI!')

computador = randint(0,10)
palpites = 0
jogador = int(input('Tente adivinhar o número: '))

if computador == jogador:
    print('Você acertou')

else:
    print('Você Errou!')
    while computador != jogador:
        palpites += 1
        jogador = int(input('Tente de novo: '))

        if jogador < computador:
            print('Mais...Tente de novo')
        elif jogador > computador:
            print('Menos...Tente de novo')
        
        if computador == jogador:
            print('Você acertou, foram necessários {} palpites para vencer de mim'.format(palpites))
#-----------------------------------------------------------------------------------------------------
059
from time import sleep
print('\033[1;31m----MENU DO LEOZIN----\033[m')
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
opção = 0
while opção != 5:
    print('''ESCOLHA ENTRE AS OPÇÕES ABAIXO
      [ 1 ] SOMAR
      [ 2 ] MULTIPLICAR
      [ 3 ] MAIOR
      [ 4 ] NOVOS NÚMEROS
      [ 5 ] ENCERRAR PROGRAMA''')
    opção = int(input('Digite sua escolha: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma dos dois números é {}'.format(soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre  os dois números é {}'.format(mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
    elif opção == 4:
        print('Digite os números novamente...')
        n1 = int(input('1° valor:'))
        n2 = int(input('2° valor:'))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('\033[31mOpção inválida. Tente novamente\033[m')
    print('=-='*10)
    sleep(2)
print('\033[34mFim do programa! Volte sempre!!!\033[m')

060 
from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))
#OU
from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}! ='.format(n), end= ' ')
while c > 0:
    print('{}'.format(c), end= ' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))

061
print('Gerador de PA')
print('-='*10)
primeiro = int(input('1° termo:'))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10 :
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM') 

062
print('Gerador de PA')
print('-='*10)
primeiro = int(input('1° termo:'))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
Mais = 10

while Mais != 0:
    total = total + Mais

    while cont <= total :
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    Mais= int(input('Mais quantos termos: ').strip())
print('Progressão finalizada com {} termos mostrados'.format(total))

063
print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)

termo = int(input('Quantos termos: '))
t0 = 0
t1 = 1
cont = 1
print('{} -> {}'.format(t0, t1), end='')
 
while cont <= termo:
    t2 = t0 + t1
    print(' -> {}'.format(t2), end='')
    t0 = t1
    t1 = t2
    cont += 1
print('-> FIM')

064
n = int(input('Digite um número (999 para parar):'))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite mais um número (999 para parar):'))
    
print('Você digitou {} números a soma deles e {} '.format(cont, soma))
------------------------------
n = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')


065
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
    


#MINHA VERSÃO
n1 = int(input('Digite um número: '))
continuar = str(input('Deseja continuar: [SIM/NÃO] ')).strip().upper()[0]
cont = 1
soma = n1
maior = n1
menor = n1
if continuar == 'S':
   while continuar == 'S':
        n = int(input('Digite mais um número: ').strip())
        continuar = str(input('Deseja continuar: [SIM/NÃO] ')).strip().upper()[0]
        soma += n
        cont += 1
        #Soma a média
        média = soma / cont
        # Maior e Menor
        if n > maior:
            maior = n
        if n < menor:
            menor = n 
        print('A soma dos {} termos digitados é {}'.format(cont,soma))
        print('A média foi de {}'.format(média))
        print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
else:
    print('\033[0;33mFIM\033[m')
    print('\033[1;31mNão foi possível realizar nenhum calculo :(\033[m')
    print('Você acabou digitando apenas {} termo'.format(cont))
    
066
#MINHA VERSÃO
soma = 0
cont = 0
while True:
    núm = int(input('Digite um número(999 para parar):'))
    if núm == 999:
        break
    soma += núm
    cont += 1
print(f'Você digitou {cont} números a soma deles é {soma}')

067
while True:
    n = int(input('Qual número deseja ver a tabuada: ').strip())
    if n < 0:
        break
    print('-'*14)
    for tabuada in range(0,11):
            print(f'{n} X {tabuada} = {n * tabuada}')
    print('-'*14)
print('\033[1;31mPrograma Finalizado! Volte sempre\033[m')

#MINHA VERSÃO
while True:
    n = int(input('Qual número quer ver a tabuada: ').strip())
    if n < 0:
        print('\033[1;31mPrograma Finalizado! Volte sempre\033[m')
        break
    else:
        print('-'*14)
        for tabuada in range(0,11):
            print(f'{n} X {tabuada} = {n * tabuada}')
        print('-'*14)

068
from random import randint
v = 0
while True:
    print('='*12)
    print('PAR OU ÍMPAR')
    print('='*12)

    jogador = int(input('Escolha um número: '))
    computador = randint(0,11)
    soma = jogador + computador

    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar: [P/I]')).strip().upper()[0]    
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {soma}')
    
    if tipo == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!! JOGUE DE NOVO')
            v += 1
        else:
             print('VOCÊ PERDEU!')
             break
   
    elif tipo == 'I':
            if soma % 2 == 1:
                print('VOCÊ VENCEU!! JOGUE DE NOVO')
                v += 1
            else:
                 print('VOCÊ PERDEU!')
                 break
            
print(f'FIM DE JOGO! VOCÊ VENCEU {v} VEZES.')
                 
069
'''MINHA VERSÃO'''
pessoas_com_18_anos = 0
homens = 0
mulher_menos_de_20 = 0

while True:
    print('-'*20)
    print('CADRASTE UMA PESSOA')
    print('-'*20)

    idade = int(input('Digite sua idade: ').strip())
    if idade > 18:
        pessoas_com_18_anos += 1

    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

    while sexo not in 'MF':
        print('\033[1;31mSexo inválido,digite novamente\033[m')
        sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()

    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_de_20 += 1

    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()
    while continuar not in 'SN':
        print('\033[1;31mSexo inválido,digite novamente\033[m')
        continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()


    if continuar == 'N':
        print('Você saiu')
        break

print(f'Total de pessoas com mais de 18 anos: {pessoas_com_18_anos}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'e temos {mulher_menos_de_20} mulheres com menos de 20 anos')

070

valor_final_compra = 0
mais_de_mil_reais = 0
mais_barato = None

while True:
    print('-'*10)
    print('  SHOPPE')
    print('-'*10)

    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$').strip())

    valor_final_compra += preco
    
    
    if mais_barato is None or preco < mais_barato:
        mais_barato = preco

    if preco >= 1000:
        mais_de_mil_reais +=1

    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar  not in 'SN':
        print('\033[1;31mErro! Digite algo válido\033[m')
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    if continuar == 'N':
        print('Obrigado Volte Sempre!')
        break
print('O valor final da compra foi de R${:.2f}'.format(valor_final_compra))
print(f'Você comprou {mais_de_mil_reais} produtos que custavam mais de R$1000,00')
print('O produto mais barato custou R${:.2f}'.format(mais_barato))