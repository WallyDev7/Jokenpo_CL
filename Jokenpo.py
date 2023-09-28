import os
from random import randrange

itens = ('pedra', 'papel', 'tesoura')

while True:

    escolha_maquina = randrange(0, 4)

    escolha_humana = int(input('''
    *** Vamos JOGA ***

    [ 0 ] - Pedra
    [ 1 ] - Papel
    [ 2 ] - Tesoura
    [ 3 ] - Sair

    ESCOLHA: '''))

    #if escolha_humana not in range(0, 4) or escolha_humana

    if escolha_humana == 3:
        print('SAINDO\nATE LOGO :D')
        break

    elif escolha_maquina == escolha_humana:
        print('EMPATE!!!')

    elif escolha_maquina == 0: #MAQUINA ESCOLHEU PEDRA
        if escolha_humana == 1: #USUARIO ESCOLHEU PAPEL
            print(':) Voce Venceu (:\n\n Voce escolheu {}\n O computador escolheu {}\n\n'.format((itens[escolha_humana].upper()), itens[escolha_maquina].upper()))
        else: #USUARIO ESCOLHEU TESOURA
            print(':( Voce Perdeu ):\n\n Voce escolheu {}\n O computador escolheu {}\n\n'.format((itens[escolha_humana].upper()), itens[escolha_maquina].upper()))

    elif escolha_maquina == 1: #MAQUINA ESCOLHEU PAPEL
        if escolha_humana == 0: #USUARIO ESCOLHEU PEDRA
            print(':( Voce Perdeu ):\n\n Voce escolheu {}\n O computador escolheu {}\n\n'.format((itens[escolha_humana].upper()), itens[escolha_maquina].upper()))
        else: #USUARIO ESCOLHEU TESOURA
            print(':) Voce Venceu (:\n\n Voce escolheu {}\n O computador escolheu {}\n\n'.format((itens[escolha_humana].upper()), itens[escolha_maquina].upper()))

    elif escolha_maquina == 2: #MAQUINA ESCOLHEU TESOURA
        if escolha_humana == 0: #USUARIO ESCOLHEU PEDRA
            print(':) Voce Venceu (:\n\n Voce escolheu {}\n O computador escolheu {}\n\n'.format((itens[escolha_humana].upper()), itens[escolha_maquina].upper()))
        else: #USUARIO ESCOLHEU PAPEL
            print(':( Voce Perdeu ):\n\n Voce escolheu {}\n O computador escolheu {}\n\n'.format((itens[escolha_humana].upper()), itens[escolha_maquina].upper()))
    
    else:
        print('OPCAO INVALIDA')
    
    input('Aperte ENTER para continuar')
    os.system('cls')
