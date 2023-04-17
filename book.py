# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Book():
    '''
    '''
    def __init__(self, title, author, year, loans):
        '''
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
        a1, a2 = self.get_author().lower(), other.get_author().lower()
        t1, t2 = self.get_title().lower(), other.get_title().lower()
        y1, y2 = self.get_year(), other.get_year()

        if a1 > a2:
            return True
        elif a1 == a2:
            if t1 > t2:
                return True
            elif t1 == t2:
                if y1 > y2:
                    return True
                else:
                    return False
    
    def get_title(self):
        '''
        '''
        return self._title
    
    def set_title(self, input_title):
        '''
        '''
        self._title = input_title

    def get_author(self):
        '''
        '''
        return self._author
    
    def set_author(self, input_author):
        '''
        '''
        self._author = input_author

    def get_year(self):
        '''
        '''
        return self._year
    
    def set_year(self, input_year):
        '''
        '''
        self._year = input_year

    def get_loans(self):
        '''
        '''
        return self._loans
    
    def set_loans(self, input_loans):
        '''
        '''
        self._loans = input_loans