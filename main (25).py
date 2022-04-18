
# Functions ( Funções )
 # DRY - Don't repeat yourselfe  
 #Parametro --> Argumento

def boas_vindas(nome, quantidade): #nome e quantidade sao Parametros
    print(f'Olá {nome}.!')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 5) #Marcos e quantidades sao Argumentos
boas_vindas('Ronaldo', 4)
boas_vindas('Linda', 2)
#Foram reduzidas as linhas usando as funçoes/ comparado com a baixo \/
'''
def boas_vindas_Marcos(): 
    print('Olá Marcos!')
    print('Temos 5 laptops em estoque')


def boas_vindas_Ronaldo(): 
    print('Olá Ronaldo!')
    print('Temos 4 laptops em estoque')


def boas_vindas_Linda(): 
    print('Olá Linda!')
    print('Temos 2 laptops em estoque')


boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Linda()
'''