import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('', key='mensagem')],  
]

window = sg.Window('Login',layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_certa = '123456'
        usuario_certo = 'caio'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_certa and usuario == usuario_certo:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Usuario ou senha incorretos')