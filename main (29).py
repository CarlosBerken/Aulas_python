# Functions ( Funções )
 # DRY - Don't repeat yourselfe  
 # Vários Argumentos (xargs) identificando Parametro.

# Criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro

print(agencia(marca='Gol', cor='Branca', motor=1.0, placa=1234))
print(agencia(marca='Gol', cor='Azul', motor=1.0,))
print(agencia(marca='Gol', cor='Preto', motor=1.0, placa=4444))

# os * nos permite utilizar um argumento e se colocar outros nos permite utilizar uma parametro