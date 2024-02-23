from unidecode import unidecode

def preprocess_search_term(search_term):
    return unidecode(search_term) if search_term else search_term
