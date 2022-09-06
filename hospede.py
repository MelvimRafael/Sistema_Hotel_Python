from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, nomeCliente, enderecoCliente, telefoneCliente, email, bairro, cep, cidade, cpfHospede):
        super().__init__(nomeCliente, enderecoCliente, telefoneCliente, email, bairro, cep, cidade)
        self.cpfHospede = cpfHospede

        
    def inserir_hospede():
        
        Hospede.nomeCliente = input('Digite seu nome: ')
        Hospede.endereco = input('Digite seu endreço: ')
        Hospede.telefone = input('Digite seu telefone: ')
        Hospede.email = input('Digite seu email: ')
        Hospede.bairro = input('Digite seu bairro: ')
        Hospede.cidade = input('Digite sua Cidade: ')
        Hospede.cpf = (input('Digite seu cpf: '))

        
        
    