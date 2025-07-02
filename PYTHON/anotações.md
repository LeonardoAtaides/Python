* TUDO EM PYTHON É UM OBJETO *

# DocString
É uma forma de "comentário", serve para anotar algo 
importante que passe de uma linha
*Fica entre três aspas* ''' ''', """ """
Ex:

'''                              """
testanto a asplas triplas   OU   testanto a asplas triplas
no python                        no python
'''                              """

# PRINT - E para algo definido ao usuário
obs:numeros geralmente não precisam de ''
para incluir um texto é apenas utilizar PRINT
Ex:
print('Olá mundo')

**TIPOS DE PRINTS**
- 1° print('A soma de 2 + 2 é', 2 + 2)
- 2° print(f'A soma de 3 + 3 é {3 + 3}')
- 3° print('A soam de 4 + 4 é {}'.format(4 + 4)) **MAIS PRÁTICA E USADA**

**MANIPULAÇÃO DE PRINTS**
*Comando Sep=''*
Utiliza-se para dar escolher um separador dentro de um print
Ex:
print(1, 2, 3, sep='-') -- 1-2-3

*Comando End= ''*
Utiliza-se para dar finalidade no final da linha de um print
Ex:
print(1, 2, 3, 4, sep='-', end='.') -- 1-2-3-4.

*Pode ser usado para manter um print na mesma linha*
Ex:
print(1, 2, 3, 4, sep='-', end='-')
print(5, 6, 7, 8, sep='-') -- 1-2-3-4-5-6-7-8

*Comando de Escape /*
Utiliza-se para colocar " por exemplo dentro de um print
Ex:
print('Hoje o dia foi \"doido\"') -- Hoje o dia foi "doido"
**Evitando um erro de sintaxe dentro do código**
**Quando deseja mostrar o caracter de escape utiliza-se:**
*Comando R*
Ex:
print(r'Hoje o dia foi \"doido\"') -- Hoje o dia foi \"doido\"
 *MAIS PRÁTICO USANDO ASPAS DIFERENTES*
Ex:
print('Hoje o dia foi "doido"') -- Hoje o dia foi "doido"

*LINHAS*
para quebrar /n, para não quebrar ao final do cod add end=' '

**PARA RETIRAR O ESPAÇO QUANDO ADIONADO** ,USA-SE '{}'.format(VARIAVEL)
OBS:deve estar dentro das''

# INPUT - entrada, usuário digita algo
Ex:
Nome = input('Qual o seu nome: ') - João
Idade = input ('Qual a sua idade: ') - 24
print('Seu nome é {} e você tem {} anos'.format(Nome, Idade))
      - Seu nome é João e você tem 24 anos -

# MANIPULAÇÃO DE STRINGS
C U R S O   E M   V I  D  E  O     P  Y  T  H  O  N
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

*FATIAMENTO- número de índice dentro da str*
**OBS:o último valor não entra na contagem**
  ex:   
frase[9] - *V*
frase[-9:] - *eo Python*- Conta de traz pra frente
frase[9:13] - *VIDE*
frase[9:21] - *VIDEO PYTHON*
frase[9:21:2] - *V D O P T O*
           |->**o "2" representa o "SALTO" de 2 espaços**
frase[:5] - *CURSO*
      |->**do inicio,0 até o 5 espaço**
frase[15:] - *PYTHON*
        |->**o 15 até o final,21**
frase[9::3] - *V E P H*
        |->**conta do 9 até o final,pulando de 3 em 3 espaço**

**COMANDO PARA STRINGS**


*LEN* - Serve para verificar a quantatidade de caracteres dentro 
de uma string
**CONTA OS ESPAÇOS DENTRO DA STRING, CUIDADO!**
Ex:
frase = 'oi'
print(len(frase)) - *2*

*REPLACE* - Serve para substituir algum elemento dentro da string
**Recebe duas coisas:**
- 1° oque vc quer substituir
- 2° qual caracter vc quer substituir

Ex: 
frase = 'estou estudando HTML'.replace('HTML', 'Python')
                                         |-> 1°   |-> 2°
print(frase) - *estou estudando Python*

**Este método pode ser chamado várias vezes na string**
Ex:
num = '123.1234.332-34'.replace('.', '').replace('-', '')
print(num) *123123433234*

                                                                       
*STARTSWITH* - Verifica se a frase começa com algo, dando reposta VERDADEIRA ou FALSA
Ex:                                                               |->**True**   |->**False**
frase = 'Olá bom dia!'
fsw = frase.startswith('Olá')
print(fsw) - *True*

*ENDSWITH* - Verifica se a frase termina com algo, dando reposta VERDADEIRA ou FALSA
Ex:                                                              |->**True**   |->**False**
frase = 'Olá bom dia!'
fsw = frase.endswith('!')
print(fsw) - True

*COUNT*- contar quantas letras tem dentro da string
Ex:
frase = 'Estudar e necessário'
f_count = frase.count('e')
print(f_count) - *3*
**Retorna sempre quantas vezes apareceu dentro da variável**

*CAPITALIZE* - Apenas a primeira letra da string fica em maiuscula*
Ex:
frase = 'amanhã será um bom dia!'.capitalize()
print(frase) - *Amanhã será um bom dia!*

*TITLE* - Deixa maiúsculo o ínicio de cada palavra*
Ex:
frase = 'o domingo a noite chegou!'.title()
print(frase)

*ISDIGIT* - Verifica na frase se contem um valor númerico, dando reposta VERDADEIRA ou FALSA
Ex:                                                                    |->**True**   |->**False**
frase = '5454'.isdigit()             frase = '5454fg'.isdigit()              
print(frase) - *True*                print(frase) - *False*

*UPPER* - Deixa todas as letras da string em maiusculas
Ex:
frase = 'um dia serei programador!'.upper()
print(frase) - *UM DIA SEREI PROGRAMADOR!*

*LOWER* - Todas as letras da frase em minusculas*
Ex: 
frase = 'AMANHÃ E DIA DE TRABALHAR!'.lower()
print(frase) - *amanhã e dia de trabalhar!*


*FIND* - Serve para encontrar algo dentro da string
**Retorna o índice onde inicia a palavra definida**
Ex: 
frase = 'Hoje e sábado ainda bem!'                     frase = 'Hoje e sábado ainda bem!'
ffd = frase.find('ainda')                              frase.find('android') 
print(ffd) - *[7]* (Onde começa a palavra 'ainda')     print(ffd) - [-1] ( Ou seja, Não existe)
              |-> **índice**

*RFIND* - encontrar pelo lado direito
Ex:
frase = 'Hoje e sábado ainda bem!'
frfd = frase.rfind('e')
print(frfd)v - *[21]* (Sempre procura até o último termo)
                 |-> **índice**

*STRIP* - Remove todos espaços desde o inicio até o final
      A P R E N D A    P  Y  T  H  O  N
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
            *onde 'A' se torna 0*
Ex:
frase = ' Aprenda Python '.strip()
print(frase) - *Aprenda Python*

*RSTRIP* -Remove apenas espaços do lado direito 'R'
EX:
frase = ' Aprenda Python  '.rstrip()
print(frase) - * Aprenda Python*

*LSTRIP* - Remove apenas espaços do lado esquerdo 'l'
EX:
frase = ' Aprenda Python  '.lrstrip()
print(frase) - *Aprenda Python *

*SPLIT* - dividir,onde se existir espaços na str*
obs:gera uma lista com todas as palavras de uma cadeia de caracteres
ex:
|C U R S O| |E M| |V I D E O| |P Y T H O N|
|0 1 2 3 4| |0 1| |0 1 2 3 4| |0 1 2 3 4 5|
     0        1        2            3

Ex:
frase = ' Rua Agusta 150, Centro, SP'
fsplit = frase.split(',')
print(fsplit) - *['Rua Agusta 150', 'Centro', 'SP']*

*TITLE* - Deixa maiúsculo o ínicio de cada palavra*
Ex:
frase = 'o domingo a noite chegou!'.title()
print(frase)

*JOIN* - Faz uma junção com elementos da strin
**Precisa ser declarado dentro de uma variável, ou terá um erro**
Ex:
frase = '12345'
f_join = '-'.join(frase)
print(f_join)

*IN* - Verifica se existe tal palavra na frase, dando reposta VERDADEIRA ou FALSA
                                                              |->**True**   |->**False**
Ex:
frase = 'o domingo a noite chegou!        frase = 'o domingo a noite chegou!
sn = 'dia' in frase                       sn = 'noite' in frase
print(sn) - *False*                       print(sn) - *True*

*IS ISTANCE()* - verifica o tipo se e str, int, float
**primeiro e passo a variável e depois o tipo: str, int, float e etc**
Ex:
lista = {'leozin', 19}

for item in lista:
    if isinstance(item, str):
        print(item.upper())
    else:
        print(item) - *LEOZIN , 19*

# TIPOS DE INFORMAÇÃO
- INT = NÚMEROS INTEIROS - 2,7,-3,9876
- FLOAT = NÚMEROS REAL - 4.5,0.076,-15.223
- BOOL =  True, False
- STR = 'Olá','7,5'
- COMPLEX = complex(1j)
- LISTA = ['Maça, 'Morango]
- TUPLA = ('A', 'B')
- RANGE = Range(6)
- DICIONÁRIO = (nome='Odemir', age=26)
- SET = sset(('A', 'B', 'C'))
- FRONZET = frozenset(('A','B', 'C'))
- BYTES = bytes(5)
- BYTEARRAY = bytearray(5)
- MEMORYVIEW = memoryview(bytes(5))

# Conversão de Tipos
É um ato para converter um tipo em outro
*Tipos imutáveis e primitivos*
Ex:
*INT*
- print(int('1') + 1) -- *2*
*FLOAT*
- print(float('1.34') + 1) -- *2.34*
*STRING*
print(str(11) + 'b') -- *11b*
*BOOL*
print(bool('')) - *False*
print(bool(' ')) - *True* 


# OPERADORES MATEMÁTICOS
+ SOMA, - SUBTRAÇÃO, * MULTIPLICAÇÃO, / DIVISÃO
** POTÊNCIA, // DIVISÃO INTEIRA, % RESTO DA DIVISÃO, **(1/2) RAIZ 

**adicao** = 10 + 10
print('Adição', adicao) -- *20*

**subtracao** = 10 - 5
print('Subtração', subtracao) -- *5*

**multiplicacao** = 10 * 10
print('Multiplicação', multiplicacao) *100*

**divisao** = 10 / 3  # float
print('Divisão', divisao) -- *3.3333333333333335*

**divisao_inteira** = 10 // 3
print('Divisão inteira', divisao_inteira) -- *3*

**exponenciacao** = 2 ** 10
print('Exponenciação', exponenciacao) -- *1024*

**modulo** = 55 % 2  # resto da divisão
print('Módulo', modulo) -- *1*

# ORDEM DE PRECEDENCIA:
1-(), 2-** , 3-* / // %, 4- + - 

# OPERADORES DE COMPARAÇÃO
1 - == IGUAL A
2 - != DIFERENTE
3 - > MAIOR
4 - < MENOR
5 - >= MAIOR IGUA
6 - <= MENOR IGUAL

# OPERADORES LÓGICOS
1 - and E
2 - or OU
3 - not NÃO

# OPERADORES DE IDENTIDADE
- IS está ali  / True e False
- IS NOT não está  / True e False

# OPERADORES DE ASSOCIAÇÃO
- IN verificar algo esta ali  / True e False
- NOT IN verificar se não está  / True e False

# TYPE - TIPO
VARIAVEL - isnumeric() - e um número? ex:1,2,3
VARIAVEL - isalpha() - e uma letra? ex: abc
VARIAVEL - isalnum() - tem alfabeto e número ex: 3a

n=input('Digite algo:')
print('é um número?',n.isnumeric())
print('é do alfabeto?',n.isalpha())
print('é dos alfanumerico?',n.isalnum())


# LISTAS - São criadas usando [] - Colchetes
Ex:
lista = [1, 2 ,3 ,4]
print(lista)

TUPLAS - São criadas usando () - Parenteses #são imutaveis
Ex:
tupla = (1, 2 ,3 ,4 )
print(tupla)

DICIONÁRIOS - São criados usando {} - Chaves
dicionario = {'Index': 'Valor', 'id1': 1, 'id2':2, 'nome': 'José'}
print(dicionario)

# CORES NO TERMINAL
# TEXT - TEXTO - cor do texto  |      BACK - COR DO FUNDO  |  STYLE - COMPORTAMENTO 
          30 - branco          |         40 - branco       |    0 - nada (None)
          31 - vermelho        |         41 - vermelho     |    1 - negrito (Bold)
          32 - verde           |         42 - verde        |    4 - sublinhado (Underline)
          33 - amarelo         |         43 - amarelo      |    7 - inverte ás configurações
          34 - azul            |         44 - azul         |
          35 - roxo            |         45 - roxo         |
          36 - ciano           |         46 - ciano        |
          37 - cinza           |         47 - cinza        |

Ex:
print('\033[1;31;43mOlá mundo!\033[m')

Ex2:
nome = 'Leozin'
cores = {'limpa': '\033[m', 
         'Azul': '\033[34m', 
         'Verde': '\033[32m', 
         'Cinza': '\033[37m'}
print('Muito prazer em te conhecer, {}{}{}!'.format(cores['Verde'],nome,cores['limpa']))



**MANIPULAÇÃO DE LISTAS**

# 1 - * APEEND() - Para adicionar um item ao final da lista *
# 2 - * LEN() - Calcular o tamanho da lista *
# 3 - * [] - Acessar posições *
# 4 - * DEL() - Excluir um elemento *
# 5 - * CLEAR() - Limpar a lista *
# 6 - * INSERT() - Para inserir um item da lista em um índice especificado *
*obs* lista.insert(0, 5)
                  |  |-> Depois o valor(str, int, float...)
                  |-> primeiro add o indice

# 7 - * EXTEND() - EStende a lista *
# 8 - * REMOVE() - Remove o item especificado *
# 9 - * POP() - Remove o índice especificado *
# 10 - * SORT() - Ordenar os valores * (reverse=True) - Inverte a ordem
# 11 - * COPY() - Faz uma cópia da Lista *
# 12 - * INDEX() - Mostra a numeração do elemento lista *
# 13 - * CONCATENA LISTAS -- += -= *

# PACOTES EXTERNO
*incluir uma ''biblioteca''*
*comando IMPORT,add a biblioteca geral*
*comando FROM-variavel-IMPORT,sendo mais especifico*

# PACOTE DATE.TIME - Datas
Ex:                                         *Importando uma biblioteca específica*
import datetime                               from datetime import date
data_hoje = datetime.datetime.today()         data_hoje = date.today()
print(data_hoje) - 2024-06-11 23:11:43        print(data_hoje) - 2024-06-11

                         Obs: A data vem no padrão americano 24/06/11 
                        para modificar usamos: data.strftime('%d/%m/%y') - 11/06/24
# PACOTE TIME - Tempo/Hrs
Ex:
import time
print('Valindo o seu acesso...')
time.sleep(3)
print('Acesso liberado!')

# BIBLIOTECA MATH - Matemática
- CEIL- faz um arredondamento para cima
- FLOOR-faz um arredondamneto para baixo
- TRUNC- elimina da virgula pra frente sem fazer arredondamento
- FACTORIAL- para calculo de fatorial
- MIN - valor minimo de uma variavel
- MAX -  valor máximo de uma varriavel
- ABS - transforma um valor negativo em positivo
- POW - Transforma o valores dentro de () em pôtencia
- SQRT- para calcular raiz quadrada

-- PARA USO GERAL USAMOS:IMPORT-MATH
-- PARA SER ESPECÍFICO USAMOS:FROM-MATH-IMPORT-SQRT 
OBS:SE IMPORTAR DUAS ADD,COMO SQRT,CEIL DE ACORDO COM A LINHA ACIMA

Ex:*GERAL*
import math
num=int(input('Digite um número:'))
raiz=math.sqrt(num)
print('a raiz de {} é igual a {}'.format(num, math.floor(raiz)))

Ex:*ESPECÍFICA*
from math import sqrt
num=int(input('Digite um número:'))
raiz=sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))

Ex:*ESPECÍFICA COM DUAS ADICIONAIS*
from math import sqrt, floor
num=int(input('Digite um número:'))
raiz=sqrt(num)
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))

# BIBLIOTECA RANDOM - Aleatório
Ex:*CHOICE - Escolha*
import random
Lista = [1, 2, 3, 4, 5, 6, 7, 8]
num= random.choice(Lista)
print(num)

Ex:*RANDOM* - gera um número aleatório entre 0 e 1
import random
num=random.random()
print(num)

ex:*RANDINT* - gera um número inteiro aleatório, *dentro de um período*
import random
num=random.randint(1, 10)
print(num)

# BIBLIOTECA STATISTICS - Estatísticas
        *Import statistics*

- MEAN - Calcula a média
- SUM - Soma os valores
- MEDIAN - Extrai a médiana 
- MODE - Calcula a moda 

# BIBLIOTECA DECIMAL - para arrendondar números decimais com muitas casas decimais
    *import decimal*
ex:
import decimal
numero = decimal.Decimal('0.2')
numero1 = decimal.Decimal('0.7')
print(numero + numero1) -- *0.9*


#   IF = SE ELIF = CONDIÇÃO  ELSE = SENÃO

IF carro.esquerda():
  bloco true

ELSE:
  bloco false

  ex1:
  nome = str(input('Qual o seu nome? '))
if nome == 'Leonardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome e tão normal!')
 print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

   #OU

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS!')

# CONDIÇÕES ANINHADAS
else + if = elif:

ex:
nome = str(input('Qual o seu nome? '))
if nome == 'João':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'José':
    print('O seu nome e bem comum no Brasil !')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))


# LAÇOS DE REPETIÇÃO - LOOP FOR
C - VARIAVEL

ex1: 
for c in range(0, 6):
    print('oi')
print('Fim')

ex2:
for c in range(6, 0, -1):
    print(c)
print('Fim')

ex3:
for c in range(0, 7, 2):
    print(c)
print('Fim')

ex4:
n = int(input('Digite um número: '))
for c in range(0, n+1): #+1 para chegar ao número digitado
    print(c)
print('FIM')

ex5:
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

ex6:
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n # s = s + n
print('O somatório de todos os valores foi {}'.format(s))

 # ESTRUTURA DE REPETIÇÃO WHILE - QUANDO NÃO HÁ LIMITE DE REPETIÇÃO
 obs: te  que dizer a ele quando parar se não se torna um loop 

ex:
while not maça:
    passo
pega
---------------------
while not maça:
    if chão:
    passo
    if buraco:
    pula
    if moeda:
    pega
pega

ex1:

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

ex2:
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

ex3:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

ex4:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))



*Para mitigar erros no código*
# BREAK
*serve para parar um código em if,elif, else*
Ex:
Lista = ['Morango', 'Pera', 'Uva', 'Abacaxi']

for frutas in Lista:
    print(frutas)
    if frutas == 'Uva': - Morango, Pera, Uva
        break

# CONTINUE
*Serve para da continuação ao código,podendo pular uma informação irrelevante*
Ex:
for Loop in range(0, 11):
    if Loop == 5:
        continue
    print(Loop)

# RETURN
*Serve para dar um retorno de valores das funções*
Ex:
def soma (x, y):                
    return x + y
variavel = soma(1, 3)
print(variavel) - *4*
**possibilita alocar os valores dentro de uma variável**

# ESTRUTURA TRY - PERMITE TESTAR UM BLOCO DE CÓDIGO QUANTO A ERRO
# EXCEPT - Permite que você lide com o erro
# ELSE - Permite executar código quando não há erro
# FINALLY - Permite que você execute código, indepedente do resultado dos blocos try e except
Ex:
try:
    0/0
    print('Deu certo meu script!')
except:
    print('Não deu certo')
finally:                                                       
    print('Vai ser executado da mesma forma!!!')


# DEF
Funções sãoo trechos de código usadas para replicar determinada ação 
ao longo do seu código
**ESTRUTURA DE FUNÇÕES - É UM BLOCO QUE SÓ E EXECUTADO QUANDO É CHAMADO**
*Usa-se para códigos simples e complexos*

Ex:01
def mensagem():
    print('Aprendendo Python!!')
mensagem()

Ex:02
def somar(Valor_1, Valor_2):
    cal =  Valor_1 + Valor_2
    print(cal)
    
somar(10, 10) - 20

**A *def* é definida em um Escopo** -  significa o local onde aquele código pode atingir.
OBS: sempre se define de dentro para fora de um código

Existe o escopo *global* e *local*:
**O escopo *global* é o escopo onde todo o código é alcançavel.**
*OBS: Não e indica usar desta forma*
Ex:
x = 1
def escopo():
    global x
    x = 10

**O escopo *local* é o escopo onde apenas nomes do mesmo local**
Ex:
x = 1
def escopo():
    x = 10

# RETURN - exclusivo apenas para funções
*Serve para dar um retorno de valores das funções*
*o return para a execução do código após ser declarado*
Ex:
def soma (x, y):                
    return x + y
variavel = soma(1, 3)
print(variavel) - *4*
**possibilita alocar os valores dentro de uma variável**

# CLOSURE "ADIANDO A EXECUÇÃO DE UMA DEF(FUNÇÃO)"
Usa-se para adiar a execução de determinada função no momento
Ex:

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args): |
    def executa():               | Define uma função interna para 
        return funcao(*args)     | realizae tal atraso na execução
    return executa               |

soma_com_cinco = criar_funcao(soma, 5 , 3)
multiplica_por_dez = criar_funcao(multiplica, 10, 2)


print(soma_com_cinco())
print(multiplica_por_dez())

# Higher Order Functions -Funções de primeira classe
E basicamente para definir que as funções podem ser tratadas
como qualquer outro tipo de dado
**Uma funcão retornando outra**
Ex:
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Bom dia', 'Leozin')) *Bom dia. Leozin*


#  Dicionários (tipo dict) 
são estruturas de dados do tipo par de "chave" e "valor". Chaves podem ser consideradas como o "índice",como: str, int, float, bool, tuple, etc.
*Usamos as chaves - {} - ou a classe dict para criar dicionários*
**Mutável: dict, list**
EX: 
pessoa = {
     'nome': 'Luiz Otávio',
     'sobrenome': 'Miranda',
     'idade': 18,     'altura': 1.8,
     'endereços': [
        {'rua': 'tal tal', 'número': 123},#         {'rua': 'outra rua', 'número': 321},
      ]
}
 pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

*Métodos dentro de dicionário*

# Métodos úteis dos dicionários em Python
*len* - quantas chaves
Ex: **print(len(dicionário))**

*keys* - Retorna o nome das chaves
Ex: **print(dicionário.keys())**

*values* - Retorna os valores dentro das chaves
Ex: **print(dicionário.values())**

*items*- Retorna os valores das chaves e os dados dentro dela
Ex: **print(dicionário.items())**

*setdefault* - adiciona valor se a chave não existe
Ex: **dicionário.setdefault('idade', 0)**
    **print(pessoa['idade'])**

*copy* - retorna uma cópia rasa (shallow copy)
Ex:
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}
d2 = d1.copy()
print(d2)

**Tem como fazer uma copia profunda**
Importa o módulo *copy*
E usa o método  *DEEPCOPY*
Ex:
Import copy             |-> o método que garante a cópia profunda
produtos_copia = copy.deepcopy(variavel)
|-> várial de cópia                 |-> passa a váriavel que deseja fazer
                                        a cópia
*-GARANTE QUE SE OS DADOS FOREM ALTERADOS NA VARIÁVEL PRINCIPAL SE ATUALIZE NA CÓPIA-*


*get* - obtém uma chave,buscando pela chave ou variável
Ex:
pessoa['Nome'] = 'José'
pessoa.get('Nome') - José
**se chave não existir retorna None, sendo possível alterar**
pessoa['Nome'] = 'José'
del pessoa['Nome']
print(pessoa.get('Nome', None))
                          |-> ou 'NÃO EXISTE'

*pop* - Apaga um item com a chave especificada (del)
Ex:
pessoa = {
     'nome': 'Luiz Otávio',
     'sobrenome': 'Miranda',
}

nome = pessoa.pop('nome')
print(pessoa) - *{'sobrenome': 'Miranda'}*

*popitem* - Apaga o último item adicionado
Ex:
pessoa = {
     'nome': 'Luiz Otávio',
     'sobrenome': 'Miranda',
}

ultima_chave = pessoa.popitem()
print(pessoa) - *{'nome': 'Luiz'}*

*update* - Atualiza um dicionário com outro/adiona chaves
Ex:
pessoa = {
     'nome': 'Luiz Otávio',
     'sobrenome': 'Miranda',
}

pessoa.update({                    pessoa.update(nome= idade=30, e)
    'idade': 30,           **OU**
    'endereço': 'Bahia'
})
print(pessoa) - *{'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30, 'endereço': 'Bahia'}*


**Desemcopamento e unindo dicionários**
*Usa-se* ** *para fazer uma união de dicionários*
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

**kwarks** - Argumentos nomeados 
*Como 'nome': 'Leozin' , 'idade': 18*
Ex:
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123) - *NÃO NOMEADOS: (1,2) / nome Joana / qlq 123*

# SETS - Conjuntos em Python
**São mutáveis, pórem aceitam apenas tipos imutáveis como valor interno**
**Não possui índices**
**Não garantem ordem**
- São eficientes par a remover valores duplicados de iteráveis
Ex:
s1 = set() -> vazio
s1 = {'Junio',1 ,2 ,3} -> com dados

*Removem os valores duplicados de iteráveis*
Ex:
s1 = {1 ,2, 2, 2,2 ,3}
print(s1) - *{1, 2, 3}*

# Métodos úteis:
*add, update, clear, discard*

1° add - adicionar um valor:
Ex:
s1 = set()
s1.add('Opa')
s1.add('Beleza')
print(s1) - *{'Beleza', 'Opa'}* ou *{'Opa', 'Beleza'}*

2° update - adiciona vários valores
s1 = set()
s1.update(('Opa', 'Beleza')) *{'Opa', 'Beleza'}*
print(s1)                 |-> sendo passado com imutavel para evitar do código
                              interar sobre cada caracter da string
                               sem (),*{'p', 'e', 'z', 'B', 'a', 'l', 'O'}*

3° clear - remove tudo dentro dom set:
Ex:
s1 = set()
s1.update(('Opa', 'Beleza'))
s1.clear()
print(s1) *set()*

4° discard - Elimina valores
Ex:
s1 = set()
s1.update((1, 2, 3, 4, 5))
s1.discard(1)
print(s1) *{2, 3, 4, 5}*

# Operadores úteis

1° União - Union
usa-se "|" para realizar a união entre dois ou mais sets:
**lembrando que não se repete itens repetidos**
Ex:
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3) - *{1, 2, 3, 4}*

2° Intersecção - Intersection 
Usa-se "&" para realizar a intersecção entre dois ou mais sets:
Ex:
s1 ={1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 & s2
print(s3) - *{2, 3}*

3° Diferença - Itens presentes apenas no set da esquerda 
Usa-se "-" para realizar a diferença entre dois sets:
Ex:
s1 ={1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 - s2
print(s3) - *{1}*

4° Diferença Simétrica - Itens que não estão em ambos:
Usa-se "^" para reaçizar a diferença simétrica entre dois sets:
Ex:
s1 ={1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2
print(s3) -  *{1, 4}*


# ESTRUTURA LAMBDA - E UMA FUNÇÃO ANÔNIMA
*Pode receber qualquer número de argumentos, mas tendo apenas uma expressão*
*Usa-se para códigos mais simples*

Ex:
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
lista.sort(key=lambda item: item["nome"])
print(lista) - *Aline,Daniel, Eduardo...*

Ex:
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
def exibir(lista):
    for item in lista:
        print(item)
    print()
l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])

exibir(l1)
exibir(l2)

Ex:
def executa(funcao, *args):
    return funcao(*args)

duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)


# List Comprehension - Uma forma rápida para criar listas a partir de interávies
Ex:
lista = [numero for numero in range(10)]
print(lista) - *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]*

*E possível realizar operações*

lista = [numero * 2 for numero in range(10)]
print(lista) - *[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]*


**Mapeamento de dados em list comprehension**
*transformando uma lista mais mantendo a quantidade de índices*
*gerando um nova lista*

lista = [numero for numero in range(10)]
            |-> PASSA A CONDIÇÃO ANTES
                podendo ser +, *, /, -, %   
print(lista) - *[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]*

Ex:
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep='\n') - *{'nome': 'p1', 'preco': 20} / {'nome': 'p2', 'preco': 10} / {'nome': 'p3', 'preco': 31.5}*

**Pode ter um filtro com if sendo adicionado depois do for**

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]


novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
print(novos_produtos, sep="\n") *[{'nome': 'p1', 'preco': 20}, {'nome': 'p3', 'preco': 31.5}*

# Dictionary Comprehension 
Ex:
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
       
print(dc) - *{'nome': 'CANETA AZUL', 'preco': 2.5}*
        
# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
**Todos os valroes Falsy**
lista = [] 
dicionario = {} 
conjunto = set()   
tupla = ()  
string = '' 
inteito = 0 
flutuante = 0.0  
nada = None 
falso = False  
intervalo = range(0) 

# Dir  getattr em Python
- Serve para chegar os métodos(nomes) dentro de uma string
- Usa-se o debugger no Terminal acessa o "Debub Console"
e digita dir(variável) assim vai mostrar todos os métodos dentro da sua string

# Hasattr
- Serve para checar um determinado objeto tem determinado nome lá dentro
Ex:
string = 'leo'
if hasattr(string, 'upper'):
             |        |-> passa o método me forma de string
             |-> passa a variável
print(string) - *Existe upper aqui*

# Getattr
- Permite que acesse o método com um variável armazenando uma string
com o nome do método
Ex:
string = 'leo'
metodo = 'upper'
 
if hasattr(string, metodo):
    print('Existe upper aqui') - *Existe upper aqui*
    print(getattr(string, metodo)()) - *LEO*
                    |       |-> a variável com método guardado em string
                    |-> passa a variável

else:
    print('Não existe o método', metodo)

# Interator
-Trabalha semelhante ao for acessando valores um a um
Ex:
    |->*É RESPONSÁVEL POR ARMAZENAR OS VALORES*
iterable = iterable = ['Eu', 'Estou', 'Cansado'] 
iterator = iter(iterable)  # tem __iter__ e __next__    sendo iterator = iterable.__iter__
|   |-> *É RESPONSÁVEL E ENTREGAR UM VALOR POR VEZ*
|
|-> **NÃO SABE O TAMANHO DA SUA INTERABLE**
|-> **NÃO SABE SEU VALOR ANTERIOR**
|-> **NÃO SABE SEU ÚLTIMO VALOR**
        *Sendo assim ele não possui índices*


print(next(iterator)) - *Eu*
print(next(iterator)) - *Estou*
print(next(iterator)) - *Cansado*
**Se der mais next além dos itens da variável ele da uma exceção no código(erro)**

# Generator expression:
- São funções que sabem pausar em determinada ocasião
- Os generator aguardam o comando next, assim ele economiza memória, esperando o comando
- Geralmente usa-se para navegar sequencialmente
|-> **NÃO SABE-SE O SEU TAMANHO**
|-> **NÃO SABE-SE SEU VALOR ANTERIOR**
|-> **NÃO SABE SEU ÚLTIMO VALOR**
    *Sendo assim ele não possui índices*
Ex:
generator = (n for n in range (3))
            |-> Usa-se () para referenciar a um generator

print(next(generator)) - *0*
print(next(generator)) - *1*
print(next(generator)) - *2*

# Yield
- usa dentro de uma função generator ao invés de usar return, usa-se *yield* para pausar
sendo executado *com next*

Ex:
def generator(n=0):
    yield 1 # Pausar
    yield 2 # Pausar

gen = generator(n=0)
print(next(gen)) - *1*
print(next(gen)) - *2*

Ex2:
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return

gen = generator(maximum=1000000)
for n in gen:
    print(n)

**Há como dar continuidade com um yield dentro de uma função**

def g1(n=0):
    yield 1 # Pausar
    yield 2 # Pausar

def g2 (gen):
    yield from gen() *importa a outra função para ela*
    yield 4
    yield 5
    yield 6

generator = g2(g1)
for num in generator:
    print(num)


# Raise
Usa-se para lançar exceções (erros)
Ex:
Criei uma exceção que mostra uma mensagem no erro
print(123)
raise ValueError('Deu erro meno') - *raise ValueError('Deu erro meno')*
                                        *ValueError: Deu erro meno*
Ex 2:
class MyError(Exception):
    ...
def levantar():
    raise MyError("System error")
try:                         ______________________
    levantar()              | para apresentar so a |
except MyError as error: -> | mensagem do erro sem |
    print(error)            | mostrar os caminhos  |
                       |______________________|
## Notas de Raise
Usado para adicionar uma especie de comentário no erro
EX:
class MyError(Exception):
    ...
def levantar():
    errors = MyError("SysteM error")
    errors.*add_note*("vacilou na line 10")
    raise errors
levantar() 


# Import
Importa um biblioteca por inteira
Ex:
import math
raiz = 4
math.sqrt(raiz) - *2.0*

**sendo necessário chamar o nome do modulo sempre quie for usar algum método**

# From
Importa Apenas um modulo especifico da biblioteca
Ex:
from math import sqrt
num = 16
raiz = sqrt(num)
print(raiz) - *4.0*

# As
Nomea a biblioteca com outro nome como especie de apelido
import math as *mat* -> nomeou como MAT, sendo possivel usar todos os   
                        métodos de MATH
num = 25
raiz = mat.sqrt(num)
print(raiz)

# Modularização
É possível importar um módulo em python ou seja sendo possivel trazer funções, prints e etc 
de outro arquivo(módulo) mas *não reconhece as pastas e arquivos acimado do __main__ principal
Ex:
*Cria os arquivos*
- Python_mod
- Python_main

Dentro do modulo e passado tudo que você deseja inserir                 
**Python_mod**
 ________________________
 |                      |
 |  def soma(n1, n2):   |
 |    return n1 + n2    |
 |______________________|

**Python_main**
 _______________________________
 |import Python_mod             | -> Importa o modulo todo sendo necessário chamar o nome |  Python_mod.soma()
 |import soma from Python_mod   | -> Importa apenas uma parte especifica do módulo
 |                              |
 | resultado = soma(10, 10)     | -> chamando a função do módulo e passando os valores
 | print(resultado)             | -> *20*
 |______________________________|


# Singleton
Um módulo deste so permite haver uma estancia do módulo no programa, ou seja so importa o módulo apenas uma vez
**E PADRÃO IMPORTAR APENAS UMA VEZ EM PYTHON**

# ImportLib
Permite recarrer um módulo novamente dentro de um programa
Ex:
import app_mod
*import importlib*

for i  in range(6):
    *importlib.reload(app_mod)* -> permite recaregar 
     print(i)                      o módulo


# Variáveis Livres
def fora(x):
    a = x          | Seria o a uma variável livre
    def dentro():  | pois ela não está definida dentro
        return a   | do escopo de *def dentro()* sendo possível
    return dentro  | acessá-la dentro da função *dentro*

# Locals                                            Globals
Mostra as variáveis locais do código | Mostra as variáveis globais do código
    *print(locals())*                             *print(globals())*


# Nonlocal
Define que a variável livre não e local que está no escopo podendo ser alterada no escopo da função
Ex:
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final -------> *define a que não e local* 
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b')) *ab*
print(c('c')) *abc*
print(c('d')) *abcd*

# Decorator
Este meio permite Adicionar / Remover / Restringir / Alterar
Ex:                                       *Está função e decoradora*
________________________________________
|def create_fuction(func):               | -> recebe uma função
|def execute(*args,**kwargs ):           | -> Cria uma função interna(closure)
|        for arg in args:                |(está função não será executada será
|            is_string(arg)              |        retornada sem execução)
|        result = func(*args, **kwargs)  |
|        return result                   | -> Sendo possível alterar algo antes 
|    return execute                      |       ou depois do resultado como:
|                                        | *Adicionar/Remover/Restringir/Alterar*
|________________________________________|

def invert_string(string): -> *inverte a frase da função*
    return string[::-1] -> *pega desde o primeiro índice até o último e inverte*

def is_string(param): -> *Recebe um paramêtro*
    if not isinstance(param, str): -> *Verifica se é string*
        raise TypeError('paramêtro deve ser uma string')-> *Se não lança uma exceção*


invert_string_check_param = create_fuction(invert_string)
inverted = invert_string_check_param('123')
print(inverted) *321*

# Syntax Sugar
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções

Ex:                                       *Está função e decoradora*
________________________________________
|def create_fuction(func):               | -> recebe uma função
|def execute(*args,**kwargs ):           | -> Cria uma função interna(closure)
|        for arg in args:                |
|            is_string(arg)              |       
|        result = func(*args, **kwargs)  |
|        return result                   | -> Sendo possível alterar algo antes 
|    return execute                      |       ou depois do resultado como:
|                                        | *Adicionar/Remover/Restringir/Alterar*
|________________________________________|

|<-*@create_fuction* -> passa a função inverte_string para o seu escopo
|def invert_string(string): -> 
|    return string[::-1] 
|
|def is_string(param): -> *Recebe um paramêtro*
|    if not isinstance(param, str): -> *Verifica se é string*
|        raise TypeError('paramêtro deve ser uma string')-> *Se não lança uma exceção*
|       _______________________________________________________________________
|----->|Não sendo necessário criar uma variável para receber *create_fuction* e |
       |*inverted_string* pois está tudo integrado na função inverted_string e  |
       |acima dela passamos *@Syntax Sugar*(linha1297) pra isso acontecer       |   
       |A Função *inverted_string* passa a ser a função *execute*,por isso      |
       |executado oque está dentro do escopo definido dentro dela               |
       |________________________________________________________________________|

        ANTES:
invert_string_check_param = create_fuction(invert_string)
inverted = invert_string_check_param('123')
print(inverted) *321*

        DEPOIS:
inverted = invert_string('123')
print(inverted) *321*


# Decorator com Paramêtros:
Cria como uma especie de fábrica onde o decoradores:
Ex:                                             ___________________________________________
def factory_decorator(a=None, b=None, c=None): | -> O principal recebe os argumentos       |
    def factory_fuctions(func):                | -> O 2° recebe a função                   |
        print('Decorator')                     |                                           |
                                               |                                           |
        def nested(*args, **kwargs):           | -> O 3° faz que adiar a execução da função|
            print('Nested')                    | e passa a ser a função "nova" pois foi    |
            result = func(*args, **kwargs)     | passado o *Sytax Sugar*                   |
            return result                      |___________________________________________|
        return nested
    return factory_fuctions

@factory_decorator()
def sum(x, y):
    return x + y
                                                    ________________________________________
multiply = factory_decorator()(lambda x, y: x * y) | Deste modo fica mais fácil criar       |
                                                   | novas funções                          |
ten_plus_five = sum(10, 5)                         |________________________________________|
ten_times_five = multiply(10, 5)
print(ten_plus_five)
print(ten_times_five)

# Ordem dos decoradores
*Sempre são exeutados de baixo pra cima:*
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador
__________________________________
| @parametros_decorador(nome='5') |
| @parametros_decorador(nome='4') |
| @parametros_decorador(nome='3') | -> Então a ordem fica desta forma
| @parametros_decorador(nome='2') |
| @parametros_decorador(nome='1') |
|_________________________________|
def soma(x, y):
    return x + y
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco) *15 1 2 3 4 5*

# MAX E MIN
São funções que verificam o valor máximo e minímo entre elementos
print(max(2, 7)) - *7* o maior valor
print(min(1, 10)) *1* o menor valor

# ZIP
Que faz uma união de elementos de acordo com seus índices 0 e 0, 1 e 1
**Retorna um interator, sendo possível apenas ver o valor fazendo um for**
**ou declarando dentro de list() podendo ver os valores**
*USA O VALOR DA LISTA MENOR*
Ex:
list_one = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_two = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(list_one,list_two)))*[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]*

# ZIP LONGEST
Que faz uma união de elementos de acordo com seus índices e uma biblioteca
do *itertools* , **from itertools import zip_longest**
Mais faz a interação sobre a lista maior
Ex:

from itertools import zip_longest                     _____________________________________
list_one = ['Salvador', 'Ubatuba', 'Belo Horizonte']  | Neste caso a interação será feita  |
list_two = ['BA', 'SP', 'MG', 'RJ']                   | sobre a list_two, faltando um valor|
                                                      | onde vai ser tratado pelo fillvalue|
                                                      |____________________________________|
print(list(zip_longest(list_one,list_two,fillvalue='SEM CIDADE')))
*[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG'), (SEM CIDADE, 'RJ')]* 

# COUNT
É um iterador sem fim(sendo infinito), diferente do range
**Ele está na biblioteca intertools** 
*from intertools import count*
Ex:
from itertools import count
c1 = count()

for i in c1:        
    if i > 10:      | Necessário passar uma condição a ele pois se não
        break       | irá executar infinitamente como um *WHILE TRUE:*
    print(i)
**Pode passar dois paramêtros para o COUNT**
Ex:            |-> define o "jump" entre os números
c1 = count(2, 2) 
           |-> define o número de onde irá iniciar

print(i)*2 4 6 8 10*

**Pode definir argumentos nomeados** 
    *start=* --------- *step=*
      |-> inicio         |-> pulo
Ex:
c1 = count(start=2, step=2)


# Combinations, Permutations e Product (Itertools)

# Combinations - A ordem não importa
Ex:
from itertools import combinations

def print_iter(interator):                  
    print(*list(interator), sep='\n')
    print()                                        
                                            _________Print:_________
                                           | *('João', 'Joana')*    |
people = [                                 | *('João', 'Luiz')*     | 
    'João', 'Joana', 'Luiz', 'Letícia'     | *('João', 'Letícia')*  |
]                                     |--> | *('Joana', 'Luiz')*    |
t_shirts = [                          |    | *('Joana', 'Letícia')* |
    ['Black', 'White']                |    | *('Luiz', 'Letícia')*  |
                                      |    |________________________|
]                                     |
print_iter(combinations(people, 2))---|     
                          |     |-> passa a quantidade da combinação
                          |-> passa a variável em que será realizado
                              a combinação

# Permutations - A ordem Importa
Ex:
from itertools import permutations

def print_iter(interator):
    print(*list(interator), sep='\n')
    print()                                   ________Print:_________
                                             | *('João', 'Joana')*   |
people = [                                   | *('João', 'Luiz')*    |
    'João', 'Joana', 'Luiz', 'Letícia'       | *('João', 'Letícia')* |
]                                            | *('Joana', 'João')*   |
t_shirts = [                             |-> |*('Joana', 'Letícia')* |
    ['Black', 'White']                   |   | *('Joana', 'Luiz')*   |
]                                        |   | *('Luiz', 'João')*    |
                                         |   | *('Luiz', 'Joana')*   | 
                                         |   | *('Luiz', 'Letícia')* |
                                         |   |________+5 Lines_______|
print_iter(permutations(people, 2))------|   
                          |     |-> passa a quantidade da permutação
                          |-> passa a variável em que será realizado a
                              permutação


# Product - Ordem importa e repete valores únicos
Ex:
from itertools import product

def print_iter(interator):
    print(*list(interator), sep='\n')
    print()                              _______Print:_____
                                        | *('Black', 'P')* |
people = [                              | *('Black', 'M')* |
    'João', 'Joana', 'Luiz', 'Letícia'  | *('Black', 'G')* |
]                                       | *('White', 'P')* |
t_shirts = [                            | *('White', 'M')* |
    ['Black', 'White'],                 | *('White', 'G')* |
    ['P', 'M','G'],                     |__________________|
]

print_iter(product(*t_shirts)) 
                   |    |-> passa a variável em que será o Produto
                   |-> desempacota as listas


# GROUPBY
É usado para agrupar valores, os dados necessitam estar ordenados para realizar o agrupamento
**Se for uma lista é possível usar sorted para ordenar**
Ex:
from itertools import groupby         -----> Usa o módulo *itertools*

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},           _______________Print:_________________
    {'nome': 'Fabrício', 'nota': 'A'},         | *A*                                  |
    {'nome': 'Rosemary', 'nota': 'C'},         | *{'nome': 'Luiz', 'nota': 'A'}*      |
    {'nome': 'Joana', 'nota': 'D'},            | *{'nome': 'Fabrício', 'nota': 'A'}*  |
    {'nome': 'João', 'nota': 'A'},             | *{'nome': 'João', 'nota': 'A'}*      |
    {'nome': 'Eduardo', 'nota': 'B'},          | *{'nome': 'André', 'nota': 'A'}*     |
    {'nome': 'André', 'nota': 'A'},            | *B*                                  |
    {'nome': 'Anderson', 'nota': 'C'},         | *{'nome': 'Letícia', 'nota': 'B'}*   |
]                                              | *{'nome': 'Eduardo', 'nota': 'B'}*   |
                                               | *C*                                  |
def ordena(aluno):                             | *{'nome': 'Rosemary', 'nota': 'C'}*  |
    return aluno['nota']                       | *{'nome': 'Anderson', 'nota': 'C'}*  |
                                               | *D*                                  |
student_agruped = sorted(alunos, key=ordena)   | *{'nome': 'Joana', 'nota': 'D'}*     |
groups = groupby(student_agruped, key=ordena)  |______________________________________|

for key, group in groups:
    print(key)
    for student in group:
        print(student)


# MAP
Se comporta como umas list compreshion, só que realiza o mapeamento dos dados
**Mas necessita passar uma função e um interavél dentro dos parâmetros de MAP**
*variável = map(função, interável)* -> quando pequeno pode-se usar *lambda*

Ex:

from functools import partial -> usado para "simular uma closure", recebendo a função 
                                 e um dos argumentos

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [                                  ________________ Print:__________________
    {'nome': 'Produto 5', 'preco': 10.00},   | *{'nome': 'Produto 5', 'preco': 11.0}*  |
    {'nome': 'Produto 1', 'preco': 22.32},   | *{'nome': 'Produto 1', 'preco': 24.55}* |
    {'nome': 'Produto 3', 'preco': 10.11},   | *{'nome': 'Produto 3', 'preco': 11.12}* |
    {'nome': 'Produto 2', 'preco': 105.87},  | *{'nome': 'Produto 2', 'preco': 116.46}*|
    {'nome': 'Produto 4', 'preco': 69.90},   | *{'nome': 'Produto 4', 'preco': 76.89}* |
]                                            |_________________________________________|

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

def muda_preco_produtos(produto):
    return{
        **produto, 'preco': aumentar_dez_porcento(produto['preco'])}

novos_produtos = list(map(          | Usa-se list para visualizar os dados         |
    muda_preco_produtos, produtos   | pois apenas a função MAP retorna o interável |
))

print_iter(novos_produtos)

# FILTER
É usado para filtrar dados através de *if* como exemplo, aqui usa-se o método *filter*
**Mas necessita passar uma função e um interavél dentro dos parâmetros de FILTER**
Ex:
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [                                 _________________Print:___________________
    {'nome': 'Produto 5', 'preco': 10.00},  | *{'nome': 'Produto 1', 'preco': 22.32}*  |
    {'nome': 'Produto 1', 'preco': 22.32},  | *{'nome': 'Produto 2', 'preco': 105.87}* |
    {'nome': 'Produto 3', 'preco': 10.11},  | *{'nome': 'Produto 4', 'preco': 69.9}*   |
    {'nome': 'Produto 2', 'preco': 105.87}, |__________________________________________|
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = filter(
    lambda p: p['preco'] >= 20, produtos
         |-> função               |-> interável onde ele irá buscar os dados
)

print_iter(novos_produtos)

# Reduce
Faz a redução de um iterável em um valor, **necessário importar o módulo functools**, ele
recebe três argumentos, a *função*, o *interável* e o *inicializador*

Ex:
Deseja realizar um total dos valores do produtos

from functools import reduce -> importante importar esse módulo para usar o reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def func_reduce(acumulador, produto ):
    return  acumulador + produto['preco']

total = reduce(     
    func_reduce,   --> *função*    # lambda ac, p: ac + p['preco']
    produtos,      --> *interável*
    0              --> *inicializador*
)
print(f'O total é: {total}')*O total é: 44*


# Função Recursiva
Funções que podem se chamar de volta, atuam parecida com o *for*
**úteis p/ dividir problemas grandes em partes menores, toda função recursiva deve ter:**
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
**Limitada em até 1000 execuções**

Ex: 

def recursiva (inicio=0, fim=4):

    if inicio >= fim:
        return fim
    
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

# Ambientes Vituais VENV
Um VENV carrega toda a sua instalação do Python para uma pasta no caminho escolhido, é um módulo que vamos usar para crirar ambientes virtuais, pode ser nomeado da forma que preferir, mas o mais comum é:  venv | env | .venv | .env  
        **O AMBIENTE VIRTUAL PERMITE VÁRIAS VERSÕES DIFERENTES DE FRAMEWOORKS**
- É literalmente uma pasta
- Nesta pasta vai ter a instalação do Python e tudo que estiver junto a ele
(Guardando também a versão do python podendo ter manutenção em códigos antigos)

## Como Criar um VENV
No terminal, especifimente powershell, utiliza-se o comando:
*python -m venv* (nome da pasta)

Para ativar o o VENV usa-se o comando, *.\venv\Scripts\activate*
Para desativar usa-se o comando, *deactivate*

# PIP INSTALL
para instalar bibliotecas extras para o python, usa-se o comando: *pip install - biblioteca*
para realizar uma atualização da biblioteca, **python.exe -m pip install --upgrade pip*

## Listar Oque está instalado
Utiliza-se o comando *pip freeze* para verificar as biblioteca instaladas no ambiente virtual

## Como Desistalar um PIP
Utiliza-se o comando *pip uninstall - biblioteca -y* 
**O Y é para confirmar a desinstalação da biblioteca**
 
## Ver Versões de uma biblioteca
Utiliza-se o comando *pip index versions - biblioteca*
para instalar uma versão usa o comando, *pip install - biblioteca==versão*

# REQUIREMENTS.TXT
Serve para salvar as versões de um ambiente virtual, podendo reinstalar quando desejar
            *Usa-se de forma "exclusiva" em uma venv pois se for global*
                    *ele aplica a versão em todos os códigos*

## Criar o Arquivo Requirements
usa-se o comando, *pip freeze > requirements.txt*

## Para instalar as versões do Requirements
Usa-se o comando, *pip install -r requirements.txt*

# CONTEXT MANAGER WITH - (abre e fecha)
**Para o caminho do arquivo usa-se \\ para corrigir o erro da \ no windons**
Ex:
caminho = 'C:\\Users\\leona\\OneDrive\\Documentos\\UDEMY_PTHON\\PYTHON\\Context Manager\\'
caminho += 'arquivo.txt'

Deve-se sempre abrir e fechar um arquivo, para abrir usa a função:
                **Passa dois paramêtros**

*arquivo.OPEN(caminho_arquivo, 'w')*
              |-> 1° caminho do |-> 2° o modo de leitura
                       arquivo           *(escrita)*
Para fechar usa a função:
*arquivo.CLOSE()*
**------------------MANEIRA MAIS EFICIENTE---------------------**
usando o método irá abrir e fechar automaticamente:
*with* open(caminho-arquivo, 'w') *as* arquivo:
**Para ler arquivos com acentos usa-se *encondind='utf-8'***

## Modos do Context Manager
*r* - leitura
*w* - escrita (apaga tudo antes e depois escreve)
*x* -  para criação
*a* - escreve ao final (mantém os dados de antes)
*b* -  binário
*t* - modo texto
*+* - leitura e escrita

## Métodos úteis
*write* - escreve
Ex:
with open(caminho_arquivo,'w') as arquivo:
    arquivo.write('Boa Noite!')
**Onde o "Boa Noite!" irá aparecer no arquivo.txt**

*read*  -  ler
Ex:    
with open(caminho_arquivo,'r') as arquivo:
print(arquivo.read())

*seek* - move o cursor
Ex:
arquivo.seek(0,0)

*readlines* - ler linha por linha
Ex:
with open(caminho_arquivo,'r') as arquivo:
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

*writelines* escrever várias linhas
Ex:
with open(caminho_arquivo,'w') as arquivo:
    arquivo.writelines(                 
        ('Bom Dia!\n', 'Boa Tarde!\n', 'Boa Noite!\n' )
    )

## Módulo OS
importa o módulo *import os*
**Sempre passa o caminho do arquivo**

*os.remove ou unlink* - apaga o arquivo
Ex:
os.remove(caminho_arquivo)

*os.rename* - troca o nome e move o arquivo
Ex:
os.remove(caminho_arquivo, 'arquivo_renomeado.txt')

# JSON
Serve para salvar ou transportar dados,Utiliza A biblioteca *json*. A estrutura de dados *json* é muito simples, não suportando coisas que executando ações específicas, como funções, métodos, classes, sets, suporta apenas dados que podem ser convertidos de python para json, **Recomendado para projeto pequenos**

## JSON DUMP ()
Serve para jogar os dados para um outro arquivo, onde com esse método ele cria um arquivo e joga os dados lá, **dentro do dos () recebe dois parametros o objeto e o arquivo**
Ex:
with open('arquivo.json', 'w') as arquivo:
    json.dump(pessoa, arquivo)
                |       |-> *Arquivo*
                |-> *Objeto*
**Passando o *ensure_ascii=False* para salvar os dados com todos os acentos nas strings**
**Passando o *indent=2* para identar os dados, deixando mais organizado visualmente**
Ex:                                  |-> Permite que as strings permaneça com acentos
with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)        
                                    |               |-> deixa o dados identados
                                    |->Permite que as strings permaneça com acentos


## JSON LOAD ()
Serve para carregar um arquivo, onde já há dados armazenados, onde ele executará a conversão
de json para python, utlizando *json.load* mais dentro de uma variável
Ex:
with open('arquivo.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    |-> variável         |- passa o arquivo


# POSITIONAL ONLY PARAMETERS
Tudo que vem antes da barra ( / ) deve ser apenas posicional
Ex:
def soma(a, b,/, c, d):
    ...
soma(1, 2 ,3, y=3)

# KEYWORD ONLY ARGUMENTS
Trabalha sozinho usando ( * ), não puxa os dados como o *args*
 Ex:
def soma(a, b, *, c):
    ...
soma(1, 2, c= 3)


# PROGRAMAÇÃO ORIENTADA A OBJETOS

## CLASS
classes ssão moldes para criar novos objetos, gerando novos objetos (instânciais) que podem
ter seus próprios atributos e métodos, onde são gerados por uma classe podem usar seus dados 
internos para realizar várias ações,
**Usa o método do PascalCase ou seja as primeiras letras de cada palavra em maiúsculo**
Ex:
class Pessoa:
|   ...
|-> E dentro da classe e necessário que utilizamos os comandos:

__init__ = *serve para inicializar os atributos do objeto ou seja, definir as propriedades e valores inicias*
Ex:
class Pessoa:
    def __init__(self,): sempre passado com o **self**
                   |-> *É uma convenção de nomenclatura que se*
                       *refere à instância atual da classe*

Logo após passa os paramêtros desejados, *nome e sobrenome*:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenoome = sobrenome

Ex: Classe com método
class Carro:
    def __init__(self, nome):
        self.nome = nome
    
##          Método
    def acelerar(self, ):
        print(f'{self.nome} está acelereando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

### Ex: Uma classe pessoa com input do usuário
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    

name = str(input('nome: ').strip().capitalize())
years = int(input('idade: ').strip())
sex = str(input('sexo: ').strip())

pessoa = Pessoa(name, years, sex)
print(f'Nome: {pessoa.nome}\nIdade: {pessoa.idade}\nSexo:{pessoa.sexo}')


### Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')

c1 = Camera('Canon')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

## Ex:
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_Vindas(self):
        print('Olá Seja Bem Vindo! {}'.format(self.Nome))

    def Recusado(self):
        print('Seu acesso foi negado!!')

    def Maior_Idade(self):
        if self.Idade >=18:
            print('Usuário é maior de Idade')
            self.Boas_Vindas()
        else:   
            print('Usuário é menor de Idade')
            self.Recusado()
            
dados = Pessoa ('Claudio', 19)
dados.Maior_Idade()

## Atributos de classe
Cria-se uma variavél como atributo da classe para que possa ser usada no restante do código,
tendo o mesmo valor em todas as instâncias da classe

### Ex:
class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p = Pessoa('Ataídes', 20)
print(p.get_ano_nascimento())


## Dict 
Ele é uma espécie de dicionário, que está dentro do objeto nas instâncias, onde mantém os valores que podem ser escritos dentro do objeto - __dict__
            **É possível alterar o valor do __dict__ é Apagar Também**
Ex:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade                      
                                      |-> Mostra todos os dados salvos do objeto
p = Pessoa('Ataídes', 20)             |
print(p.__dict__) - *{'nome': 'Ataídes', 'idade': 20}*

## Vars
Vai mostrar o __dict__ da variável que está sendo usada
Ex:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa('Ataídes', 20)
print(vars(p)) - *{'nome': 'Ataídes', 'idade': 20}*



## @PROPERTY e GETTER
É um método que utilizado para obter ter um valor de determinado atributo
-Para evitar quebrar código "cliente" -> **é o código que usa seu código**
-Para Habilitar setter
-Para executar ações ao obter um atributo

Ex: 
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
                                   _____________________________________________________
    def get_cor(self):     -----> |proteje a cor dentro de um escopo evitando de quebrar|
        return self.cor_tinta     |o código ao realizar a troca de nome                 |
                                  |_____________________________________________________|
caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.get_cor())


*@property* é um propriedade do objeto, que se comporta como um atributo, sendo usada:
**Não é necessário chamar o método com "()", apenas acessar o atributo**
-Também permite desta forma não quebrar o código cliente


Ex:
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    @property
    def cor(self):
        return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)

## SETTER
É um método que é utilizado para configurar determinado atributo
- Passa por um método para configurar o atributo
- Evitar quebrar código 

Ex: 
class Caneta:
    def __init__(self, cor):       _______________________________________________________
        self.__cor = cor # -----> | o __ é nome da variável significa não use este método |
                                  | fora da classe *Private Protected*                    |
                                  |_______________________________________________________|

    @property                   _________*Recebe o valor*______
    def cor(self):      -->    | traz o valor do init para den |
        return self.__cor      | tro do método que excuta ações|
                               |_______________________________|

     |-> nome da property      ___________________*Configura o Valor*_____________________
    @cor.setter                |         Recebe um valor que vem do *property*             |
    def cor(self, valor): ---> | Possível realizar um lógica com if para fazer um filtro   |
        self.__cor = valor     |___________________________________________________________|
    
caneta = Caneta('Azul')
caneta.cor = 'Rosa'

# ENCAPSULAMENTO
São modificadores de acesso: public, protected, private mas como o 
python *não tem* segue as covenções:

*Sem underline = public*: Pode ser usado em qualquer lugar

*_ Um underline = protected*: Não deve ser usado fora, mas sim dentro da classe e subclasses

*__ Dois underlines = private*: Só deve ser usado na classe em que foi declarado, especilmente um dev

# ASSOCIAÇÃO
É uma ligação entre duas ou mais classes, que tem uma relação entre os objetos, sendo uma relação fraca

# AGREGAÇÃO
As duas coisas existem de forma independente, mas juntas agregam para algo maior
Ex: Relação de 1 pra vários, um Carrinho de compras pra vários produtos

class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum(p.preco for p in self._produtos)
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}")  
        print()
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
carrinho = Carrinho()
p1, p2 = Produto("Camiseta", 20.0),Produto("Calça", 25.0)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(f"Total: {carrinho.total()}")

# COMPOSIÇÃO
É uma relação de agregação forte, ou seja quando o objeto "pai" for apagado, todas as referências dos objetos "filhos" também são apagados
Ex:
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1
print(endereco_externo.rua, endereco_externo.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')


# Herança 
Uma classe extende a outra classe por herença, sendo usada para deixar uma classe mais genérica para ser utilizada em outras
Ex:
        *Classe Principal(pessoa)*       |      *Classes filhas (cliente)*
-> super class, base class, parent class | -> sub class, clild class, derived class
        **Acima Hierarquicamente**       |       **Abaixo Hierarquicamente**

Ex:
class Pessoa:
    def __init__(self, nome,sobrenome):
        self.nome= nome
        self.sobrenome = sobrenome
    
    def falar_nome(self):
        print(self.nome, self.sobrenome,self.__class__.__name__)
class Cliente(Pessoa):
    ...

c1 = Cliente('Leonardo', 'Ataídes')
print(c1.nome, c1.sobrenome)
c1.falar_nome()

# Herança Multipla
Uma classe pode estender várias classes 
Ex: 
Log -> FileLog ------ Humano -> Pessoa -> Cliente
          *Cliente(Pessoa, FileLog)*


## Super 
É uma classe que retorna temporiamente a super classe, permitindo chamar os métodos dela
ex: 
class MinhaString(str):            _____________________________
    def upper(self):              |Se não colocar retorna *None*|
        super()                   |_____________________________|

string = MinhaString('ataídes')
print(string.capitalize())

##  Sobreposição
Sobrescrever um método da super classe na sub classe
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        return super().upper()

string = MinhaString('ataídes')
print(string.upper())

# Classes Obstradas (ABC)
São usadas como contratos para a definição de novas classes,podendo forçar outras classes
a criarem métodos concretos, podem ter métodos concretos por elas mesmas

_@abstractmethods_ são métodos que não têm corpo, as regras para as classes abstratas com 
métodos abstratos é que elas não podem ser instãnciadas diretamente

_Métodos abstratos_ devem ser implementados nas subclasses (@abstractmethod)

Uma classe abstrata em Pyhton tem sua metaclasse sendo _ABCMeta_

É possível criar @property @setter @classmethod @staticmethod e @nethod como abstratos, para isso,
usar @abstractmethod como decorador mais interno

Ex:
from abc import ABC, abstractmethod 

class Log(ABC): -> herda de ABC
    @abstractmethod -> decorator que mantém a classe abstrata
    def _log(self, msg):...


    def log_error(self,msg):
       return self._log(f'Error: {msg}')
    
    def log_success(self,msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
       msg_formatada = f'{msg} ({self.__class__.__name__})'
       print('Salvando no log:', msg_formatada)
       with open(LOG_FILE, 'a') as arquivo:
           arquivo.write(msg_formatada)
           arquivo.write('\n')

# POLIMORFISMO
É o principio que permite qiue as classees derivadas de uma mesma superclasse tenham métodos iguais com a mesma assinatura, mas com comportamentos diferentes

*príncipio da substituição de liskov*
- Objetos de uma superclasse dever ser substituíves, por objetos de uma subclasse sem quebrar a aplicação

Ex:
from abc import ABC, abstractmethod
class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)


## DUNDER METHODS
São métodos que realiza certa ação quando o objeto é instanciado
__lt__(self,other) - self < other
__le__(self,other) - self <= other
__gt__(self,other) - self > other
__ge__(self,other) - self >= other
__eq__(self,other) - self == other
__ne__(self,other) - self != other
__add__(self,other) - self + other
__sub__(self,other) - self - other
__mul__(self,other) - self * other
__truediv__(self,other) - self / other
__neg__(self) - -self
__str__(self) - str
__repr__(self) - str



# COMANDO ROUND - para arrendondar números
**round()**
Ex:
Valor_exemplo = 123.999
r = round(Valor_exemplo)
print(r)


#  Dicionários (tipo dict) 
são estruturas de dados do tipo par de "chave" e "valor". Chaves podem ser consideradas como o "índice",como: str, int, float, bool, tuple, etc.
*Usamos as chaves - {} - ou a classe dict para criar dicionários*
**Mutável: dict, list**
EX: 
pessoa = {
     'nome': 'Luiz Otávio',
     'sobrenome': 'Miranda',
     'idade': 18,     'altura': 1.8,
     'endereços': [
        {'rua': 'tal tal', 'número': 123},#         {'rua': 'outra rua', 'número': 321},
      ]
}
 pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

*Mètodos dentro de dicionário*
.get - Ele tenta obter uma chave,busando pela chave ou variável
Ex:
pessoa['Nome'] = 'José'
pessoa.get('Nome') - José
**se chave não existir retorna None, sendo possível alterar**
pessoa['Nome'] = 'José'
del pessoa['Nome']
print(pessoa.get('Nome', None))
                          |-> ou 'NÃO EXISTE'


# ID -- Identidade
Ex:
v1 ="a"
print(id(v1)) -- *140712393133280*

# None = Não valor

# Operadores de atribuição
= += -= *= /= //= **= %=

contador = 10

contador /= 5
print(contador)

# Iterável -> str, range, etc (__iter__)
*Iterador*-> quem sabe entregar um valor por vez
*next* -> me entregue o próximo valor
*iter* -> me entregue seu iterador

# Listas em Python
**Tipo list - Mutável** -Suporta vários valores de qualquer tipo
*Métodos úteis*:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

# Empacotamento e Desempacotamento
_  -> pode servir para se atribuir algum valor
*_ -> serve para aderir o resto de valores
ex:
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)

Ex:
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p, b, *_, ap, u = lista
print(p, u, ap)

**PARA DAR UM PRINT NO DESEMPACOTAMENTO**
# print(*lista) - *Maria Helena 1 2 3 Eduarda*

# Enumerate - enumerador
enumera uma iteráveis (índices)
Ex:

lista = ['Maria', 'Helena', 'Luiz']
lista_enumerada = enumerate(lista)

print(next(lista_enumerada))

for item in lista_enumerada:
    print(item)

"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')



# Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>

# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')