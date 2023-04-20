# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from array_ordered_positional_list import ArrayOrderedPositionalList as PositionalList1
from linked_ordered_positional_list import LinkedOrderedPositionalList as PositionalList2
from book import Book

def create_book_from_line(params):
    '''
    Creates a book from a line of information of the .txt file that the program is running through.

    Paramenters
    -------------
    params: str
        line of text that contains the book's information.
    Returns
    ----------
    Book(título,autor,año,prestamos)
        Book class object containing the book's data.

    '''
    titulo, autor = params[0:2]
    año, prestamos = int(params[2]), int(params[3])
    
    return Book(titulo, autor, año, prestamos)

def create_book_list(path, t):
    '''
    Creates a books list.

    Paramenters
    -------------
    path: file
        Name of a file in the actual directory.
    t: int
        Number used to choose which positional list to generate.
    Returns
    ----------
    Book(título,autor,año,prestamos)
        Book class object containing the book's data.

    '''
    with open(path) as f:
        if t == 1:
            book_list = PositionalList1()
        else:
            book_list = PositionalList2()

        for elemento in f.readlines():
            book_list.add(create_book_from_line(elemento.split('; ')))
            
    return book_list

def print_menu():
    '''
    Prints a text menu.

    Parameters
    ----------
    None.

    Returns
    ----------
    None.
    '''
    print('\n————————SISTEMA DE BIBLIOTECA—————————\n')
    print('OPCIONES:')
    print('-> 1. Leer un fichero y crear una lista ordenada de libros (sobreescribe la lista actual).')
    print('-> 2. Determinar la media de préstamos.')
    print('-> 3. Eliminar libros con mismo título y autor, dejando la versión más reciente.')
    print('-> 4. Consultar los libros que quedan en la biblioteca.')
    print('->     4a. Todos.')
    print('->     4b. Por año.')
    print('->     4c. Por autor.')
    print('-> 5. Mostrar este menú.')
    print('-> 6. Cerrar el programa.\n')

def ask_for_option(max_options: int):
    '''
    A function that prints a line of text asking the user to choose an option of the menu

    Parameters
    ------------
    max_options: int
        Int used to limit the max amount of options in the menu.
    
    Returns
    -----------
    opt: int
        The chosen option.

    '''
    while True:
        try:
            opt = int(input('Introduzca la opción que desee utilizar: '))
            if not 1 <= opt <= max_options:
                raise TypeError()
            else:
                break            
        except TypeError:
            print('Esa opción no está entre los números válidos.')
        except:
            print('Eso no es un número.')
    
    return opt

def avg_loans(bl):
    '''
    A functions that calculates AND prints the average number of loans of a list of books.

    Parameters
    ------------
    bl: List
        The list of books you want to calculate an average of.

    Returns
    ------------
    None.

    '''
    sum, n = 0, 0
    for libro in bl:
        sum += libro.get_loans()
        n += 1
    print('La media es de {} préstamos.'.format(round(sum/n, 2)))

def remove_duplicates(bl):
    '''
    A function that removes duplicates books from a list of books.

    Parameters
    ------------
    bl: List
        The list of books you want to remove the duplicates of.

    Returns
    ------------
    unique_books: list
        The new list, with the same books but with the duplicates removed.
    '''
    unique_books = bl
    marker = unique_books.last()
    
    while unique_books.before(marker) != None:
        prev = unique_books.before(marker)
        marker_book, prev_book = unique_books.get_element(marker), unique_books.get_element(prev)
                
        if marker_book.get_title() == prev_book.get_title() and marker_book.get_year() >= prev_book.get_year():
            unique_books.delete(prev)
        else:
            marker = unique_books.before(marker)
                
    return unique_books

def show_books(bl, t):
    '''
    A function that prints all current books according to different filters and criteria..

    Parameters
    -----------
    bl: List
        list of books that the function will operate on.
    t: int
        Number used to choose which positional list to generate.

    Returns
    -------
    None.
    '''
    valid_options = ['a', 'b', 'c']
    while True:
        suboption = input('Introduzca opción a, b o c: ')
        if suboption not in valid_options:
            print('Esa opción no es válida. Por favor, introduzca otra.')
        else:
            break
    
    if suboption == 'a':
        lista_a_imprimir = bl
    else:
        if t == 1:
            lista_a_imprimir = PositionalList1()
        else:
            lista_a_imprimir = PositionalList2()

    if suboption == 'b':
        while True:
            try:
                año = int(input('Introduzca el año para consultar los libros publicados durante el mismo: '))
                break
            except:
                print('Debe introducir un número.')

        for libro in bl:
            if libro.get_year() == año:
                lista_a_imprimir.add(libro)

    elif suboption == 'c':
        while True:
            try:
                autor = input('Introduzca el autor para consultar los libros que ha publicado: ')
                break
            except:
                print('Debe introducir un número.')

        for libro in bl:
            if libro.get_author() == autor:
                lista_a_imprimir.add(libro)
        pass
    
    print('\n———————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    print('|  {:<37}|  {:<30}|  {:<18}|  {:<17}|'.format('Título', 'Autor', 'Año de edición', 'Nº de préstamos'))
    print('———————————————————————————————————————————————————————————————————————————————————————————————————————————————————')
    for libro in lista_a_imprimir:
        print('|  {:<37}|  {:<30}|  {:<18}|  {:<17}|'.format(
            libro.get_title(),
            libro.get_author(),
            libro.get_year(),
            libro.get_loans()
        ))
    print('———————————————————————————————————————————————————————————————————————————————————————————————————————————————————\n')        

if __name__ == "__main__":
    tipo_de_lista = 2
    lista_de_libros = None
    
    print_menu()

    while True:
        option = ask_for_option(6)
        if option == 1:
            while True:
                ruta = input('Introduzca el nombre del archivo que desea utilizar (debe estar en el mismo directorio): ')
                try:
                    lista_de_libros = create_book_list(ruta, tipo_de_lista)
                    break
                except:
                    print('Esa ruta de archivo no es válida. Por favor, introduce otra.')
        
        elif option == 2:
            if lista_de_libros == None:
                print('Debes ejecutar la opción 1 primero.')
            else:
                avg_loans(lista_de_libros)
        
        elif option == 3:
            if lista_de_libros == None:
                print('Debes ejecutar la opción 1 primero.')
            else:
                lista_de_libros = remove_duplicates(lista_de_libros)
                print('Hecho.')
        
        elif option == 4:
            if lista_de_libros == None:
                print('Debes ejecutar la opción 1 primero.')
            else:
                show_books(lista_de_libros, tipo_de_lista)
                
        elif option == 5:
            print_menu()
            
        elif option == 6:
            print('Cerrando el programa...\n')
            quit()