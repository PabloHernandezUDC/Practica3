# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from array_ordered_positional_list import ArrayPositionalList as PositionalList
from linked_ordered_positional_list import LinkedPositionalLIst as PositionalList


def parse_params(params):
    '''
    '''
    a, a = params[0], params[1]
    
        
    return None # Objeto de la clase libro

def run(path):
    '''
    '''
    with open(path) as f:
        for elemento in f.readlines():
            a = parse_params(elemento.split())

    return stats

if __name__ == "__main__":
    result = run(sys.argv[1])