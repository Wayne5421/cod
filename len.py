nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome == ' ' and idade == ' ' :
    print('você não digitou nada')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome ao contrario é {nome[::-1]}')
    if ' ' in nome:
        print('seu nome possui espaço')
    else:
        print('seu nome não tem espaços')
    print(f'seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')