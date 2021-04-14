class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls): #acessar dados da propria classe
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        #cumprimentar_da_classe=Pessoa.cumprimentar(self)  #chama cumprimentar da classe Pessoa, classe pai
        cumprimentar_da_classe=super().cumprimentar()  #chama cumprimentar da classe Pessoa, classe pai
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Homem(renzo, nome='Luciano')  #renzo é um filho de luciano
    print(Pessoa.cumprimentar(luciano))  #utilizei o método cumprimentar a partir da classe Pessoa c/ o parametro luciano
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)  # qual é o nome de luciano
    print(luciano.idade)  # qual é a idade de luciano
    for filho in luciano.filhos:  # para cada filho em filhos de luciano
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' # add atributo dinamicamente
    del luciano.filhos  # deletar atributos
    luciano.olhos = 1
    del luciano.olhos
    print(renzo.__dict__)  # para ver todos os atributos do luciano
    print(luciano.__dict__)   # para ver todos os atributos do renzo
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))  # True. o objeto pessoa é uma instancia da classe Pessoa
    print(isinstance(pessoa, Homem))  # False. o objeto pessoa não é uma instancia da classe Homem
    print(isinstance(renzo, Pessoa))  # True. o objeto pessoa é uma instancia da classe Pessoa
    print(isinstance(renzo, Homem))  # True. o objeto pessoa é uma instancia da classe Homem
    print(isinstance(renzo, Mutante))  # True. o objeto pessoa é uma instancia da classe Homem
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())