# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Libro():
    '''
    '''
    def __init__(self, title, author, year, loans):
        '''
        '''
        self.title = title
        self.author = author
        self.year = year
        self.loans = loans
    
    def get_title(self):
        '''
        '''
        return self.title
    
    def set_title(self, input_title):
        '''
        '''
        self.title = input_title

    def get_author(self):
        '''
        '''
        return self.author
    
    def set_author(self, input_author):
        '''
        '''
        self.author = input_author

    def get_year(self):
        '''
        '''
        return self.year
    
    def set_year(self, input_year):
        '''
        '''
        self.year = input_year

    def get_loans(self):
        '''
        '''
        return self.loans
    
    def set_loans(self, input_loans):
        '''
        '''
        self.loans = input_loans