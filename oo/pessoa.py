class Pessoa:
"""
    >>>print(Pessoa.cumprimentar(luciano))
"""
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls): #acessar dados da propria classe
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')  #renzo é um filho de luciano
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
    print(luciano.__dict__)  # para ver todos os atributos do luciano
    print(renzo.__dict__)   # para ver todos os atributos do renzo
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())