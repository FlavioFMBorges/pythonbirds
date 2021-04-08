class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')  #renzo é um filho de luciano
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:  # para cada filho em filhos de luciano
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' # add atributo dinamicamente
    del luciano.filhos  # deletar atributos
    print(luciano.__dict__)  # para ver todos os atributos do luciano
    print(renzo.__dict__)   # para ver todos os atributos do renzo
