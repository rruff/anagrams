""" Utility functions """

def sort_chars(word):
    """ Sort the characters in `word` alphabetically. """
    if word is None:
        return None
    
    return ''.join(sorted(list(word)))