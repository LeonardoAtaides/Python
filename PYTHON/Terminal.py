from itertools import product

def print_iter(interator):
    print(*list(interator), sep='\n')
    print()

people = [
    'João', 'Joana', 'Luiz', 'Letícia'
]
t_shirts = [
    ['Black', 'White'],
    ['P', 'M','G'], 
    ['Woman','Men']
]

print_iter(product(*t_shirts))