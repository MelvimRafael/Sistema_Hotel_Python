from tipoQ import TipoQ


class Quarto:
    def __init__(self, numero, situacao):
        self.numeroQ = numero
        self.situacao = situacao


    def menu_quarto():
        while True:
            print(' QUARTOS DISPONIVEL')
            print('-'*20)
            print('[1] - QUARTO SIMPLES')
            print('[2] - QUARTO LUXO')
            print('[3] - QUARTO DUPLO')
            print('[4] - QUARTO CASAL')

            quarto = int(input('Digite uma opção: '))
            
            if quarto == 1:
                TipoQ.simples()


            elif quarto == 2:
                print(TipoQ.luxo)

            elif quarto == 3:
                    pass

            elif quarto == 4:
                    pass

            else:
                print('Opção inválida!')
                break
                menu_quarto()
                
    def tipo_quarto():
        print ('Qaurto luxo')
        

    def tipo_quarto():
        pass
    # menu_quarto()        