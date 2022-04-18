
# Functions (Funções)
 #DRY - Don't repeat yourself.
# Realizam uma tarefa
# Calcula e retorna um Valor

def cliente1(nome):
    print(f'Olá {nome}')


def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('Jose')

print(x)

# se quer so uma tarefa, utiliza o print / se for usado depois utiliza o return para jogar na memoria e depois jogar na tela