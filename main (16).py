
compra_confirmada = False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra')