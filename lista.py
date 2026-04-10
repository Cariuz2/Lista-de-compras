import os

print('Lista de compras \n ____________________')

entrada = '1'
lista = []
item = ''
valor = ''
while True:

    entrada = input('Escolha uma das opções abaixo: \n' \
    '1. Adicionar itens na lista;\n' \
    '2. Apagar itens na lista; \n' \
    '3. Listar os valores da lista;\n' \
    '4. Encerrar e imprimir a lista.\n')

    entradas_permitidas = '1234'

    if entrada not in entradas_permitidas:
        print('Número inválido.')
        continue
    ########################################################################################################################
    # ADD

    if entrada == '1':
        os.system('cls' if os.name == 'nt' else clear)
        item = input('Nome do item: ')
        lista.append(item)
        continue

    # DELETE
    
    if entrada == '2':
        os.system('cls' if os.name == 'nt' else clear)
        valor = input('Índice do item: ')
        try:
            lista.pop(int(valor))
        except:
            print('Valor de índice inválido')
            continue


    # VIEW

    if entrada == '3':
        os.system('cls' if os.name == 'nt' else clear)
        for indice, item in enumerate(lista):
            print(indice, item)
        continue

    # STOP

    if entrada == '4':
        os.system('cls' if os.name == 'nt' else clear)
        for indice, item in enumerate(lista):
            print(indice, item)
        break
    