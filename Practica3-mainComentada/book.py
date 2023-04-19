# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Book():
    '''
    A class used to represent a book.

    ...

    Attributes
    ----------
    title : str
        a string that contains the book's title.
    author : str
        a string that contains the book's author.
    year : int
        an int that means the year the book was published
    loans : int
        an int that means the number of loans that that the book has.

    Methods
    -------
    __gt__(other = Book)
        Magic method used to compare books and solve a draw situation.
    __ge__(other = Book)
        Same as __gt__()
    '''
    def __init__(self, title, author, year, loans):
        '''
        Parameters
        ----------
    title : str
        a string that contains the book's title.
    author : str
        a string that contains the book's author.
    year : int
        an int that means the year the book was published
    loans : int
        an int that means the number of loans that that the book has.
        '''
        self._title = title
        self._author = author
        self._year = year
        self._loans = loans
        
    def __gt__(self, other):
        a1, a2 = self.get_author().lower(), other.get_author().lower()
        t1, t2 = self.get_title().lower(), other.get_title().lower()
        y1, y2 = self.get_year(), other.get_year()
        
        if a1 > a2:
            return True
        elif a1 < a2:
            return False
        elif t1 > t2:
            return True
        elif t1 < t2:
            return False
        elif y1 > y2:
            return True
        elif y1 < y2:
            return False
        
    def __ge__(self, other):
        return self > other
        
    
    def get_title(self):
        '''
        function used to get the title of a book
        Parameters
        ----------
        None
        

        Returns
        ----------

        title: str
            Title of the book
        '''
        return self._title
    
    def set_title(self, input_title):
        '''
        Function used to change a book's title.
        Parameters
        ----------
        input_title: str
            new title for the book.
        

        Returns
        ----------
        None.

        
        '''
        self._title = input_title

    def get_author(self):
        '''
        Function used to get the author of a book.

        Parameters
        ----------
        None.
        

        Returns
        ----------

        author: str
            Author of the book.
        '''
        return self._author
    
    def set_author(self, input_author):
        '''
        Function used to change a book's author.
        Parameters
        ----------
        input_author: str
            new author for the book.
        

        Returns
        ----------
        None.

        
        '''
        self._author = input_author

    def get_year(self):
        '''
        Function used to get the publishment year of a book.

        Parameters
        ----------
        None.
        

        Returns
        ----------

        year: int
            Year when the book was published.
        '''
        return self._year
    
    def set_year(self, input_year):
        '''
        Function used to change a book's publishment year.
        Parameters
        ----------
        input_year: int
            new publishment year for the book.
        

        Returns
        ----------
        None.
        '''
        self._year = input_year

    def get_loans(self):
        '''
        '''
        return self._loans
    
    def set_loans(self, input_loans):
        '''
        Function used to get the number of loans of a book.

        Parameters
        ----------
        None.
        

        Returns
        ----------

        input_loans: int
            Book's number of loans.
        '''
        self._loans = input_loans