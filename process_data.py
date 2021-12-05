from pandas import read_csv
from pandas import read_excel
from numpy import array

def process_excel(filepath):
    raw_data = read_excel(filepath)
    return raw_data

def process_csv(filepath):
    raw_data = read_csv(filepath)
    return raw_data