# 01
nome = str('Leonardo')
sobrenome = str('Ataídes')
idade = int(18)
ano_nascimento = int(2005)
maior_idade = idade >= 18
altura = float(1.71)

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_idade)
print('Altura em metros:', altura)

#02
nome = 'Leozin'
altura = 1.71
peso = 68
imc = peso / altura ** 2 # ou peso / (altura * altura)

print(f'{nome} tem {altura}, pesa {peso} kilos, o seu IMC é {imc:.2f}')

#03
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

if n1 > n2:
    print(f'O maior numero é {n1} o menor é {n2}')
elif n1 == n2:
    print(f'Os números {n1} e {n2} são iguais!')
else:
    print(f'O maior número é {n2} o menor é {n1}')

#04
#minha versão com ajuda chat e pesquisa
nome = (input('Digite seu nome: ')).strip()
idade = (input('Digite sua Idade: '))

if not nome or not idade or nome and idade == ' ':
    print('Desculpe, Você deixou campos vazios')

else:
    n_letras = len(nome)
    primeira_letra =(nome[0])
    ultima_letra = (nome[-1])
    espacos = nome.count(' ')

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem um total de {espacos} espaços')
    print(f'Seu nome tem {n_letras} letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')
    
#Do professor
nome = (input('Digite seu nome: '))
idade = (input('Digite sua Idade: '))

if  nome and idade:

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contêm espaços')
    else:
        print('Seu nome NÂO contêm espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
   print('Desculpe, Você deixou campos vazios')


#05
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# CHAT AJUDOU A LEMBRAR SOBRE TRY E EXCEPT
numero = input('Digite um número inteiro para ver se é PAR ou ÍMPAR: ')

try:
    numero_int= int(numero)

    if numero_int % 2 == 0:
        print(f'O número {numero_int} é PAR')
    elif numero_int % 2 == 1:
        print(f'O número {numero_int} é ÍMPAR ')

except:
    print('Este número não é um inteiro')

#VERSÃO DO PROFESSOR

if entrada.isdigit():
     entrada_int = int(entrada)
     par_impar = entrada_int % 2 == 0
     par_impar_texto = 'ímpar'

     if par_impar:
         par_impar_texto = 'par'

     print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
-------------------------------------------------------
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')


#06
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Que horas são? ').strip()
horas_int = int(horas)

if horas_int >= 0 and horas_int <= 11:
    print('BOM DIA MEU BOM!!')

elif horas_int >= 12 and horas_int <= 17:
    print('BOA TARDE FILHINHO DE PAI!')

elif horas_int >=18 and horas_int <=23:
    print('BOA NOITE MEU REI')

else:
    print('Vá dormir')


#VERSÃO PROFESSOR

entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input('Digite seu nome: ')
contagem_letras = len(nome)

if contagem_letras <= 4:
    print('Seu nome é curto!')

elif contagem_letras >= 5 and contagem_letras <= 6:
    print('Seu nome é normal!')

elif contagem_letras > 6:
    print('Seu nome é muito grande!')
    
#VERSÃO DO PROFESSOR

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
    
#07
'''Quase descobri, por um  sinal de = desisti e vi a resolução :/'''
nome = 'José Alberto'
tamanho_string = len(nome)
cont = 0
novo_nome = ''


while cont < tamanho_string:
    letra = nome[cont]
    novo_nome += f'*{letra}'
    cont += 1

print(novo_nome)

#08
'''Calculadora com while'''
# MINHA VERSÃO
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        
        operador_permitidos = '+-/*'

    except:
        print('\033[1;31mErro! Você digitou algo não válido\033[m')
        continue
    
    operador = input('Digite o operador: (+, -, /, *): ')

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'A soma dos numeros {num_1_float} e {num_2_float} é igual {soma} ')

    elif operador == '-':
        subtracao = num_1_float - num_2_float
        print(f'A subtração dos números {num_1_float} e {num_2_float} é igual {subtracao}')
            
    elif operador == '/':
        divisao = num_1_float / num_2_float
        print(f'A divisão dos números {num_1_float} e { num_2_float} é igual {divisao}')
            
    elif operador == '*':
        multiplicacao = num_1_float * num_2_float
        print(f'A multiplicação dos números {num_1_float} e {num_2_float} é igual {multiplicacao}')
            
    elif len(operador) > 1:
        print('\033[1;31mErro!!\033[m Digite Apenas um operador!')

    elif operador is not operador_permitidos:
        print('\033[1;31mErro!!\033[m Isto não é um operador')
            
    sair = input('Deseja encerrar o programa? [Sim/Não]').lower().startswith('s')
   
    if sair is True:
        print('Programa encerrado!!')
        break

#09 Não consegui fazer por completo
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0
while True:
    
    letra_digitada = input('Digite uma letra:')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada= ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta    
        else:
            palavra_formada += '*'

    print(f'Palavra formada:{palavra_formada}')
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!!!!')
        print(f'A PALAVRA ERA {palavra_secreta}')
        print(f'Tentativas: {tentativas}')

        letras_acertadas = ''
        tentativas = 0
    break

---------------------------------------------

"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
""" 
**MINHA VERSÃO**

lista = ['Maria', 'Helena', 'Luiz', 'Jeorge']
tamanho_lista = len(lista)
i = 0

while i < tamanho_lista:
    print(f'{i} {lista[i]}')
    i += 1

# Professor
"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
-------------------------------------------------------------
# MINHA VERSÃO COM AJUDA DO CHAT PARA POUCAS COISAS
"""
Faça uma lista de compras com listas]
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista
não permita que o programa quebre com erros de índices inixistentes na lista.
"""
lista = []
while True:
    print('Selecione uma Opção:')
    opcao = input('[i]inserir [a]apagar [l]listar: ').lower()[0]
    

    if opcao in ['i', 'a', 'l']:

        if opcao == 'i':
            valor = input('Valor:')
            lista.append(valor)
            print(lista)
    
        elif opcao == 'a':
            if not lista:
                print('Não há nada para apagar')
                  
            else:
                apagar = input('escolha o índice que queira apagar: ')
                indice = len(lista)

                if apagar.isdigit():
                    apagar_int = int(apagar)
                    if apagar_int < indice:
                        print('OK APAGANDO...')
                        lista.pop(apagar_int)
                        print(f'A lista atualizada fica {lista}')

                    else:
                        print('Nâo existe este indice na sua lista!') 

                else:
                    print('Digite algo válido')
           
        elif opcao == 'l':
            if not lista:
                print('Não há nada para listar')

            else:
                for indice, nome in enumerate(lista):
                    print(indice, nome)
            
    else:
        print('Digite algo válido')
    break

# VERSÃO DO PROFESSOR
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
    break

# MINHA VERSÃO DE CÓDIGO

#CÓDIGO OTIMIZADO

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
'''
Calculo do segundo dígito do CPF
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
'''
'''
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
'''
'''
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
'''

# VERIFICANDO O PRIMEIRO DIGITO

'''CPF PADRÃO SEM ALTERAÇÕES'''
cpf = '746.824.890-70'
'''CPF APENAS COM OS 9 DIGITOS PARA MULTIPLICAÇÃO'''
cpf_nove_digitos = cpf[0:11]
'''CPF DIVIDIDO PARA TIRAR OS PONTOS "."'''
cpf_divisao = cpf_nove_digitos.split('.')
cpf_formatado = ''.join(cpf_divisao)
'''CPF APENAS OS NÚMEOROS E FORMATADO EM INTEIRO PARA MULTIPLICAÇÃO'''
cpf_formatado_int = int(cpf_formatado)


print(f'{cpf}')
print(f'{cpf_nove_digitos}')
print(f'{cpf_divisao}')
print(f'{cpf_formatado_int}')

'''MULTIPLICAÇÃO DOS DIGITOS'''
resultados_mult_digito_1 = []
num_regressivos_dig1 = 10

for digito in cpf_formatado:
    digito_int = int(digito)
    resultado = digito_int * num_regressivos_dig1
    print(f'{digito_int} X {num_regressivos_dig1} = {resultado}' )
    resultados_mult_digito_1.append(resultado)
    num_regressivos_dig1 -= 1
print(resultados_mult_digito_1)

'''SOMA DOS NÚMEROS DO RESULTADO DA MULTIPLICAÇÃO'''
soma_digito_1 = sum(resultados_mult_digito_1)
print(soma_digito_1)
''' MULTIPLICAÇÃO POR 10 '''
multi_10_digito_1 = soma_digito_1 * 10
print(multi_10_digito_1)
'''RESTO DA DIVISÃO POR 11'''
resto_div_digito_1 = multi_10_digito_1 % 11
print(resto_div_digito_1)
'''VALIDAÇÃO DO PRIMEIRO DIGITO'''
'''Operação ternária'''
digito_1_validado = resto_div_digito_1 if resto_div_digito_1 <= 9 else 0
print(digito_1_validado)
'''-----------------------------------------'''
'''OUTRA MANEIRA'''
'''
 if resto_div <= 9:
    print(resto_div)
else:
    print('0')
'''

### VERIFICANDO O SEGUNDO DIGITO

'''CPF + PRIMEIRO DIGITO VÁLIDADO'''
cpf_formatado_2 = cpf_formatado + str(digito_1_validado)
print(cpf_formatado_2)

'''MULTIPLICAÇÃO DOS DIGITOS'''
resultados_mult_digito_2 = []
num_regressivos_dig2 = 11
for digito_2 in cpf_formatado_2:
    digito_2_int = int(digito_2)
    resultado_d2 = digito_2_int * num_regressivos_dig2
    print(f'{digito_2} X {num_regressivos_dig2} = {resultado_d2}')
    resultados_mult_digito_2.append(resultado_d2)
    num_regressivos_dig2 -= 1
print(resultados_mult_digito_2)

'''SOMA DOS NÚMEROS DO RESULTADO DA MULTIPLICAÇÃO'''
soma_digito_2 = sum(resultados_mult_digito_2)
print(soma_digito_2)
'''MULTIPLICAÇÃO POR 10'''
multi_10_digito_2 = soma_digito_2 * 10
print(multi_10_digito_2)
'''RESTO DA DIVISÃO POR 11'''
resto_div_digito_2 = multi_10_digito_2 % 11
print(resto_div_digito_2)
'''VALIDANDO O SEGUNDO DIGITO'''
digito2_validado = resto_div_digito_2 if resto_div_digito_2 <= 9 else 0
print(digito2_validado)

# MENSAGEM DE VÁLIDAÇÃO
novo_cpf = f'{cpf_nove_digitos}-{digito_1_validado}{digito2_validado}'

if cpf == novo_cpf:
    print(f'{cpf} é válido!')
else:
    print('CPF inválido')

#VERSÃO DO PROFESSOR

cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')



# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar (*args):
    n_mult = 1
    for num in args:
        n_mult *= num
    return n_mult

resultado = multiplicar(1, 2, 3, 4, 5)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
#Retorne se o número é par ou ímpar

def par_impar(numero):
    multiplo_de_dois = numero % 2 ==0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    

print(par_impar(35))
print(par_impar(26))


#MINHA VERSÃO
# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
numero = int(input('Digite um número: '))

def duplicar (dobro):
    dobro = numero * 2
    return f'O dobro de {numero} é {dobro}'

def triplicar (triplo):
    triplo = numero * 3
    return f'O triplo de {numero} é {triplo}'

def quadruplicar (quadruplo):
    quadruplo = numero * 4
    return f'O quadruplo de {numero} é {quadruplo}'

print(duplicar(numero))
print(triplicar(numero))
print(quadruplicar(numero))

#VERSÃO DO PROFESSOR MAIS OTIMIZADO!
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))



#MINHA VERSÃO
# Exercício - sistema de perguntas e respostas
# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

pergunta_1 = perguntas[0]['Pergunta']
pergunta_2 = perguntas[1]['Pergunta']
pergunta_3 = perguntas[2]['Pergunta']
lista_opcao = ['a)', 'b)', 'c)', 'd)']
item = 0
item2 = 0
item3 = 0
acertos = 0

while True:
    print('*'*23)
    print(' PERGUNTAS E RESPOSTAS')
    print('*'*23)

    
    print(f'\n{pergunta_1}')
    for opcao in perguntas[0]['Opções']:
        print(lista_opcao[item],opcao)
        item +=1
    
    resposta = input('Digite a resposta: ').strip().upper()

    if resposta not in 'ABCD':
        print('Digite algo válido')
    else:
        if resposta == 'C':
            print('\033[1;32mAcertou!\033[m')
            acertos +=1
        else:
            print('\033[1;31mErrou!!\033[m')

    print(f'\n{pergunta_2}')
    for opcao in perguntas[1]['Opções']:
        print(lista_opcao[item2], opcao)
        item2 +=1
    
    resposta = input('Digite a resposta: ').strip().upper()

    if resposta not in 'ABCD':
        print('Digite algo válido')
    else:
        if resposta == 'A':
            print('\033[1;32mAcertou!\033[m')
            acertos +=1
        else:
            print('\033[1;31mErrou!!\033[m')
            print(f'\n{pergunta_2}')

    print(f'\n{pergunta_3}')
    for opcao in perguntas[2]['Opções']:
        print(lista_opcao[item3], opcao)
        item3 +=1
    
    resposta = input('Digite a resposta: ').strip().upper()

    if resposta not in 'ABCD':
        print('Digite algo válido')
    else:
        if resposta == 'B':
            print('\033[1;32mAcertou!\033[m')
            acertos +=1
        else:
            print('\033[1;31mErrou!!\033[m')
    break

print(f'\nVocê acertou {acertos} de {len(perguntas)} perguntas')


# VERSÃO DO PROFESSOR


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')

"""
Exercício VERSÃO DO PROFESSOR - NÃO CONSEGUI FAZER
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista in lista_de_listas_de_inteiros:
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    ) 

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from modulos import produtos
import copy

novos_produtos = copy.deepcopy(produtos)



produtos_ordenados_por_preco = [
    {**novo_preco, 'preco': f"{novo_preco['preco'] * 1.10:.2f}"}
    for novo_preco in novos_produtos
]

produtos_ordenados_por_produto = copy.deepcopy(produtos)
produtos_ordenados_por_produto.sort(key=lambda item: item['nome'])

produtos_ordenados_por_produto_preco = copy.deepcopy(produtos_ordenados_por_preco)
produtos_ordenados_por_produto_preco.sort(key=lambda item: item['preco'])

print('PRODUTOS:')
print(*produtos, sep="\n")
print()
print('DEPOIS DO AUMENTO DE 10%:')
print(*produtos_ordenados_por_preco, sep="\n")
print()
print('ORDENADOS POR PRODUTOS:')
print(*produtos_ordenados_por_produto, sep='\n')
print()
print('ORDENADOS POR PREÇO')
print(*produtos_ordenados_por_produto_preco, sep='\n')

    





--------------------------------------------------------------------
# ANOTAÇÃO DE CÓDIGO**
velocidade =61
local_carro = 100

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')
------------------------------------------------------------------------
"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)


# Crie uma função que una a listas com o estado e 
# e sua abreviação usando todos os valores máximo da lista
list_one = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_two = ['BA', 'SP', 'MG', 'RJ']

def zipper(list1, list2):
    new_list = []
    i = 0
    for one in list1:
        new_list.append((one, list2[i]))
        i+=1
    return new_list

State_City = zipper(list_one, list_two)
print(State_City)

# VERSÃO DO PROFESSOR

def zipper(list1, list2):
    intervalo_max = (min(len(list1), len(list2)))
    return [
        (list1[i], list2[i]) for i in range(intervalo_max)
    ]

print(zipper(list_one,list_two))

"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
list_a = [10, 2, 3, 40, 5, 6, 7]
list_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

# 1° VERSÃO PROF
lista_soma = []
for i in range(len(lista_b)):
     lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

# 2° VERSÃO PROF
lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])

#MINHA VERSÃO
def List_sum(list1, list2):
    size = min(len(list1),len(list2))
    return[
        list1[i] + list2[i] for i in range(size)
    ]

print(List_sum(list_a, list_b))


# NOMEAR COM LISTAS
lista_carros = ["vw", "Audi", "Bmw"]
marca_01 , marca_02, marca_03 = lista_carros
print(marca_01, marca_02, marca_03)

# COMBINAR VARIAVEIS
nome = str('Odemir') 
sobrenome = str("depiere")
Nome_Completo = nome + ' ' +sobrenome
print(Nome_Completo)

# EXPERIMENTO NÚMERO EM STRING
nome = 'Odemir'
idade = str( 18 )
print(nome, idade,'anos')

# EXPERIMENTO 2 STRING EM NUMERO
Investimento = 1000
taxa_juros = float('0.2') 
res = Investimento * taxa_juros
print(res)
----------------------------------------------------------
#COMANDO ROUND
Valor_exemplo = 12.123473821
r = (Valor_exemplo, 4)
print(r)

#COMANDO LEN
Lista = [1, 2 , 3, 4, 5, 6, 7, ]
Dicionario = {'Nome': 'Odemir', 'Idade':29}
Tupla = (1, 2, 3)
String = 'Olá Mundo!'
len = len(String)
print(len)

# REPLACE  EX - 01
cpf = 'CPF:123456789'
num_cpf = int(cpf.replace('CPF:', '')) 
print(num_cpf)
-------------------------------------------
#BIBLIOTECA DATETIME
#01
from datetime import date
ano= date.today().year
mês = date.today().month
dia = date.today().day
print(' estamos no dia {} do mês {} do ano de {}'.format(dia, mês, ano))

#02
from datetime import date
nasc =int(input('Digite sua data de nascimento:'))
data_atual = date.today().year
idade = data_atual - nasc
print('Sua data de nascimento é {}, portanto sua idade é de {} anos'.format(nasc, idade))

#03
from datetime import date
data = date.today()
data_br = data.strftime('%d/%m/%y')
print(data_br)

#04
import datetime
data = datetime.datetime.today()
data_soma = data + datetime.timedelta(days=4)
data_br = data_soma.strftime('%d/%m/%y')
print(data_br)

#BIBLIOTECA TIME

#01
import time
time_Texto = '21 June, 2021'
t = time.strptime(time_Texto, '%d %B, %Y')
t_formatado = time.strftime('%d/%m/%y', t)
print(t_formatado) - 21/06/21

#02
import math
tupla = (10, 2, 4, 8, 22, 7,)
minimo = min(tupla)
maximo = max(tupla)
print('O valor minimo é {} e o númerom máximo é {}'.format(minimo,maximo))

#03
import math
valor = abs(-7.25)
print(valor)

#04
import math
valor = pow(3, 4)
print(valor)

#05
import math
valor = int(math.sqrt(16))
print(valor)

#06
import math
valor1 = math.ceil(1.4)
valor2 = math.floor(1.4)
print('o Valor arredondado pra cima fica {},arrendondado para baixo fica {}'.format(valor1, valor2))

# BIBLIOTECA STATISTICS

#01
import statistics
Lista = [12, 15, 28, 56, 78, 80]
média = sum(Lista) / len(Lista)
print(média)

#MAIS PRÁTUCO
import statistics
Lista = [12, 15, 28, 56, 78, 80]
média = statistics.mean(Lista)
print(média)

#02
import statistics
Lista = [12, 15, 28, 56, 78, 80]
média = statistics.median(Lista)
print(média)

#03
import statistics
Lista = [12, 15, 28, 31, 56, 78, 78, 80]
média = statistics.mode(Lista)
print(média)

# IF E ELSE

#01
usuário = int(input('Digite sua idade: '))
if usuário >= 18:
    print('Sua entrada foi autorizada, Seja bem Vindo!')
else:
    print('Você e menor de idade, Não pode entrar :/')

#02 usuário = int(input('Digite sua idade: '))
if usuário >= 18:
    print('Sua entrada foi autorizada, Seja bem Vindo!')
elif usuário == 17:
    print('Quase lá,só mais ano amigão')
elif usuário <=15:
    print('Vai estudar rapa!')
else:
    print('Você e menor de idade, Não pode entrar :/')


#LOOP RANGE

#01 
for valor in range(11):
    print(valor * 2)

#02
Lista = ['Brasil', 'uruguai', 'Equador', 'Colombia', 'Estados Unidos', 'Angola', ]
for paises in Lista:
    print(paises)
Lista = ['Brasil', 'Uruguai', 'Equador', 'Colombia', 'Estados Unidos', 'Angola', ]
-------------------------------------------------------
for paises in Lista:
    if paises == 'Brasil':
        print('O {} é hexacampeão da copa do mundo!'.format(paises))

#03
Lista = ['Brasil', 'Uruguai', 'Equador', 'Colombia', 'Estados Unidos', 'Angola', ]

for paises in Lista:
    if paises == 'Brasil':
        print('O {} é hexacampeão da copa do mundo!'.format(paises))
for paises in Lista:
    if paises == 'Uruguai':
        print('O {} é bicampeão da copa do mundo!'.format(paises))
-----------------------------------------------------------
Lista = ['Brasil', 'Uruguai', 'Equador', 'Colombia', 'Estados Unidos', 'Angola', ]
for loop in range(0, len(Lista), 2):
    print(Lista[loop])

#04
Lista = ['Brasil', 'Uruguai', 'Equador', 'Colombia', 'Estados Unidos', 'Angola', ]
for index, pais in enumerate(Lista):
    print(index, pais)

#05
lista = [x  for x in range (0, 20, 2)]
print(lista)
------------------------------------------------
lista = [x * 3 for x in range (0, 11,)]
print(lista)
-------------------------------------------
Lista = ['']
for Loop in range(0, 11):
    Lista.append(Loop)
print(Lista)

#06
loop = 0

while loop <= 10:
    print(loop)
    if loop == 5:
        for x in range(10):
            print(x)

    loop +=1


#07 joguinho

import random
while True:
    Professor = random.randint(0, 10)
    Eu = random.randint(0, 10)

    print('O professor tirou a valor {}'.format(Professor))
    print('Eu tirei o valor {}'.format(Eu))

    if Professor > Eu:
        print('O Professor Ganhou!')
        break
    
    elif Eu > Professor:
        print('Eu ganhei!!!!!')

#08 
def somar(Valor_1, Valor_2):
    cal =  Valor_1 + Valor_2
    print(cal)
    
somar(10, 10) 

#09
def somar(Valor_1, Valor_2):
    cal =  Valor_1 + Valor_2
    print(cal)

import random
for loop in range(0, 10):

    x = random.random()
    y = random.random()

    somar(x,y)

#10

def média(Valor_1, Valor_2):
    cal_média = (n1 + n2) / 2
    return cal_média # retorna o valor calculado
    

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota:'))
media = média(n1, n2)
print('A sua média foi {}'.format(media))

if media >= 7:
    print('Parabens você passou!!')
elif media < 7:
    print('Que pena você está Reprovado!')

#11
Função_soma = lambda valor_1, valor_2 : valor_1 + valor_2
soma = Função_soma(25, 5)
print(soma)

ex = lambda valor : 'Verdadeiro' if valor % 2 == 0 else 'Falso'
soma =  ex(1)
print(soma)
------------------------------------------------------------------
nota = lambda valor_1, valor_2 : (valor_1 + valor_2) / 2

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota: '))
média = nota(n1, n2)
print('Sua média final foi de {} pontos'.format(média))

 #12
class Pessoa:

#Metodo Construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print('Olá Seja Bem Vindo! {}'.format(self.Nome))

    def Recusado(self):
        print('Seu acesso foi negado!!')



# Função
    def Maior_Idade(self):

        if self.Idade >=18:
            print('Usuário é maior de Idade')
            self.Boas_Vindas()

        else:   
            print('Usuário é menor de Idade')
            self.Recusado()
            
dados = Pessoa ('Claudio', 19)
dados.Maior_Idade()



sexo = (input('Qual o seu sexo? [M/F]: ')).upper().strip()[0]

while sexo not in 'MmFf':
    print('Erro! Digite novamente!')
    sexo = input('Qual o seu sexo? [M/F]').upper()

    if sexo == 'M':
        print('O seu sexo e Masculino')

    elif sexo == 'F':
        print('O seu sexo e Feminimo')