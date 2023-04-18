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

def create_book_list(path):
    '''
    '''
    with open(path) as f:
        book_list = PositionalList1()
        for elemento in f.readlines():
            book_list.add(create_book_from_line(elemento.split('; ')))
            
    return book_list

def print_menu():
    '''
    '''
    print('\nSISTEMA DE BIBLIOTECA\n')
    print('OPCIONES:')
    print('-> 1. Leer un fichero y crear una lista ordenada de libros.')
    print('-> 2. Determinar la media de préstamos por libro.')
    print('-> 3. Eliminar libros con mismo título y autor, dejando la versión más reciente.')
    print('-> 4. Consultar que libros quedan en la biblioteca.')
    print('->     4a. Todos.')
    print('->     4b. Por año.')
    print('->     4c. Por autor.')
    print('-> 5. Cerrar el programa.\n')

def ask_for_option():
    '''
    '''
    opt = int(input('Introduzca la opción que desee utilizar: '))
    while type(opt) is not int or not 1 <= opt <= 5:
        print('Esa opción es incorrecta.')
        opt = int(input('Introduzca la opción que desee utilizar: '))
    
    return opt

def avg_loans(bl):
    sum, n = 0, 0
    for libro in bl:
        sum += libro.get_loans()
        n += 1
    print('La media de préstamos es de {}.'.format(round(sum/n, 2)))

def remove_duplicates(bl):
    unique_books = bl
    for i in range(1, len(unique_books)):
        l = len(unique_books)
        if i < l:
            libro = unique_books.get_element(i)
            prev = unique_books.get_element(i - 1)
            if prev is not None and libro.get_title() == prev.get_title() and libro.get_year() >= prev.get_year():
                unique_books.delete(i - 1)

    print('Hecho.')


def show_books(bl, suboption):
    if suboption == 'a':
        print('\n-------------------------------------------------------------------------------------------------------------------')
        print('|  {:<37}|  {:<30}|  {:<18}|  {:<17}|'.format('Título', 'Autor', 'Año de edición', 'Nº de préstamos'))
        print('-------------------------------------------------------------------------------------------------------------------')
        for libro in bl:
            print('|  {:<37}|  {:<30}|  {:<18}|  {:<17}|'.format(
                libro.get_title(),
                libro.get_author(),
                libro.get_year(),
                libro.get_loans()
            ))
        print('-------------------------------------------------------------------------------------------------------------------\n')        

if __name__ == "__main__":
    print_menu()
    lista_de_libros = None
    
    while True:
        # 1. Leer un fichero y crear una lista ordenada de libros.
        # 2. Determinar la media de préstamos por libro.
        # 3. Eliminar libros con mismo título y autor, dejando la versión más reciente.
        # 4. Consultar que libros quedan en la biblioteca.
        #     4a. Todos.
        #     4b. Por año.
        #     4c. Por autor.
        # 5. Cerrar el programa.
        option = ask_for_option()
        
        if option == 1:
            ruta = str(input('Introduzca el nombre del archivo que desea utilizar (debe estar en el mismo directorio): '))
            while type(ruta) is not str:
                ruta = str(input('Introduzca el nombre del archivo que desea utilizar (debe estar en el mismo directorio): '))
            while True:
                try:
                    lista_de_libros = create_book_list(ruta)
                    break
                except:
                    print('Esa ruta de archivo no es válida. Por favor, introduce otra.')
                    ruta = str(input('Introduzca el nombre del archivo que desea utilizar (debe estar en el mismo directorio): '))
                    while type(ruta) is not str:
                        ruta = str(input('Introduzca el nombre del archivo que desea utilizar (debe estar en el mismo directorio): '))
        
        elif option == 2:
            if lista_de_libros == None:
                print('Debes ejecutar la opción 1 primero.')
            else:
                avg_loans(lista_de_libros)
        
        elif option == 3:
            if lista_de_libros == None:
                print('Debes ejecutar la opción 1 primero.')
            else:
                remove_duplicates(lista_de_libros)
        
        elif option == 4:
            if lista_de_libros == None:
                print('Debes ejecutar la opción 1 primero.')
            else:
                subopt = str(input('Introduzca la opción a, b o c: '))
                while type(subopt) is not str:
                    subopt = str(input('Introduzca la opción a, b o c: '))

                show_books(lista_de_libros, subopt)
                
        elif option == 5:
            print('Cerrando el programa...\n')
            quit()