from hospede import Hospede
from quarto import Quarto

def menu():
    while True:
        print('-' * 21)
        print('|  HOTEL BEIRA RIO  |')
        print('-' * 21)
        print('[1] - CADASTRAR HOSPEDE')
        print('[2] - QUARTOS DISPONIVEL')
        print('[3] - ALUGA QUARTO')
        print('[4] - SERVIÇOS')
        print('[5] - SAIR')

        res = int(input('Digite uma opção: '))
        if res == 1:
            Hospede.inserir_hospede()

        elif res == 2:
            Quarto.menu_quarto()

        elif res == 3:
           pass

        elif res == 4:
            pass

        elif res == 5:
            break

        else:
            print('Opção invalida!')
            menu()
            
menu()