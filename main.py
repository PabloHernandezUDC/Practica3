# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys
from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList
from linked_ordered_positional_list import LinkedOrderedPositionalList as PositionalList
from libro import Libro

def parse_params(params):
    '''
    '''
    titulo, autor = params[0:2]
    año, prestamos = int(params[2]), int(params[3])
    
    return Libro(titulo, autor, año, prestamos)

def run(path):
    '''
    '''
    with open(path) as f:
        for elemento in f.readlines():
            a = parse_params(elemento.split('; '))

    return None

if __name__ == "__main__":
    result = run('libros.txt')