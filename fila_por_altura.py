import bisect
from random import randrange, choice


nomes = [
    'Joseph Griffin',
    'Kendra Lopez',
    'Paula Jackson',
    'Bruce Reed MD',
    'Samantha Gibson',
    'Carl Fisher',
    'Mr. Jose Anderson',
    'Heather Olson',
    'Ryan Melendez',
    'Carla Green',
    'Jasmine Smith',
    'Laurie Day',
    'Savannah Jones',
    'David Brooks',
    'Ashley Fernandez'
]


def monta_lista_pessoas(qtd=10):
    return [Pessoa(choice(nomes), randrange(150, 200)) for _ in range(qtd)]


class Pessoa:

    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def __repr__(self):
        return f'Pessoa(nome={self.nome}, altura={self.altura})'

    def __str__(self):
        return f'{self.nome} | Altura: {self.altura}'

    def __lt__(self, other):
        return self.altura < other.altura

    def __len__(self):
        return self.altura


class FilaPorAltura:

    def __init__(self, pessoas):
        self.pessoas = sorted(pessoas)

    def __repr__(self):
        return f'FilaPorAltura(pessoas={self.pessoas})'

    def __len__(self):
        return len(self.pessoas)

    def __iter__(self):
        for pessoa in self.pessoas:
            yield pessoa

    def __add__(self, other):
        return FilaPorAltura(self.pessoas + other.pessoas)

    def __getitem__(self, pos):
        return self.pessoas[pos]

    def __reversed__(self):
        raise Exception('nao pode')

    def add(self, pessoa):
        bisect.insort(self.pessoas, pessoa)
