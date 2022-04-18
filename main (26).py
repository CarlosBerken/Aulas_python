
# Functions ( Funções )
 # DRY - Don't repeat yourselfe  
 #Parametro --> Argumento
 # Default = Aquele que você define o valor do parametro
 # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(quantidade, nome='Linda'): #quantidade Default
    print(f'Olá {nome}.!')
    print(f'Temos {str(quantidade)} laptops em estoque')
    #quantidade não default
    #Non-default vem primeiro que o default / o argumento que define o valor sempre tem que estar por ultimo

boas_vindas(6)
    