import sys
# from re import sub

def load_text(filename):
    '''Reads file data'''
    with open(filename, 'r', encoding='utf-8-sig') as f:
        read_data = f.read()
    return read_data.split()