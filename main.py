# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import sys
from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList1
from linked_ordered_positional_list import LinkedOrderedPositionalList as PositionalList2
from book import Book

def create_book_from_line(params):
    '''
    '''
    titulo, autor = params[0:2]
    año, prestamos = int(params[2]), int(params[3])
    
    return Book(titulo, autor, año, prestamos)

def print_menu():
    '''
    '''
    print('\nSISTEMA DE BIBLIOTECA\n')
    print('OPCIONES:')
    print('-> 1. Leer un fichero y crear una lista ordenada con ellos.')
    print('-> 2. Determinar la media de préstamos por libro.')
    print('-> 3. Eliminar libros con mismo título y autor, dejando la versión más reciente.')
    print('-> 4. Consultar que libros quedan en la biblioteca.')
    print('->     4a. Todos.')
    print('->     4b. Por año.')
    print('->     4c. Por autor.')
    print('-> 5. Cerrar el programa.\n')

def create_book_list(path):
    '''
    '''
    with open(path) as f:
        book_list = PositionalList1()
        for elemento in f.readlines():
            book_list.add(create_book_from_line(elemento.split('; ')))
            
    return book_list

def get_avg_loans(bl):
    sum, n = 0, 0
    avg_loans = {}
    current_title = ''
    # recorrer la lista
    # almacenar el titulo actual y sumarle 1 a n
    # guardar loans en sum
    # si el titulo cambia resetear sum y n, y devolver la media
    
    for libro in bl:
        if current_title == libro.get_title():
            sum += libro.get_loans()
            n += 1
        else:
            avg_loans[current_title] = sum/n
            current_title = libro.get_title()
            sum, n = 0, 0
    
    print(avg_loans)

if __name__ == "__main__":
    print_menu()
    while True:
        option = int(input('Introduzca la opción que desee utilizar:'))