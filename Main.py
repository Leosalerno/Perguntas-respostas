import os
contador = 0
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
    {
        'Pergunta': 'Quem descobriu o Brasil?',
        'Opções': ['Pedro Álvares Cabral', 'Pero Vaz de Caminha', 'Bartolomeu Dias', 'Vasco da Gama'],
        'Resposta': 'Pedro Álvares Cabral',
    },
    {
        'Pergunta': 'Em que ano o Brasil foi descoberto?',
        'Opções': ['1450', '1498', '1550', '1500'],
        'Resposta': '1500',
    },
]
for indice, dict_atual in enumerate(perguntas):
    os.system('cls')

    print('Pergunta:', dict_atual['Pergunta'])
    for i,valor in (enumerate(dict_atual['Opções'])):
        if i == 0:
            print(f'a) {valor}')
        elif i == 1:
            print(f'b) {valor}')
        elif i == 2:
            print(f'c) {valor}')
        elif i == 3:
            print(f'd) {valor}')
    escolha = input("Escolha uma alternativa: ")
    if escolha == 'a':
        if dict_atual['Opções'][0] == dict_atual['Resposta']:
            print('Acertou😎')
            contador += 1
            input("Pressione ENTER para continuar...")
        else:
            print('Errou😓')
            input("Pressione ENTER para continuar...")
    elif escolha == 'b':
        if dict_atual['Opções'][1] == dict_atual['Resposta']:
            print('Acertou😎')
            contador += 1
            input("Pressione ENTER para continuar...")
        else:
            print('Errou😓')
            input("Pressione ENTER para continuar...")
    elif escolha == 'c':
        if dict_atual['Opções'][2] == dict_atual['Resposta']:
            print('Acertou😎')
            contador += 1
            input("Pressione ENTER para continuar...")
        else:
            print('Errou😓')
            input("Pressione ENTER para continuar...")
    elif escolha == 'd':
        if dict_atual['Opções'][3] == dict_atual['Resposta']:
            print('Acertou😎')
            input("Pressione ENTER para continuar...")
            contador += 1
        else:
            print('Errou😓')
            input("Pressione ENTER para continuar...")
    else:
        print('Errou😓')
        input("Pressione ENTER para continuar...")
    
print(f'Voce acertou {contador} perguntas de {len(perguntas)}')
    
