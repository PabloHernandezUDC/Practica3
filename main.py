# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys
from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList1
from linked_ordered_positional_list import LinkedOrderedPositionalList as PositionalList2
from libro import Libro

def create_book_from_line(params):
    '''
    '''
    titulo, autor = params[0:2]
    año, prestamos = int(params[2]), int(params[3])
    
    return Libro(titulo, autor, año, prestamos)

def create_book_list(path):
    '''
    '''
    with open(path) as f:
        book_list = PositionalList1()
        for elemento in f.readlines():
            libro_actual = create_book_from_line(elemento.split('; '))
            

    return None

if __name__ == "__main__":
    result = create_book_list(sys.argv[1])