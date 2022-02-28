import pandas as pd
import numpy as np

'''
# reads csv-file with pandas
#
# args:
# path : path to .csv file
# head : (default: None) 0, if the .csv-File has a Head for every col
# seperator : character that used to seperate coloumns (default: None)
# format - bool : decide, if the data should be transposed or not (default: True)
#
# returns:
# numpy.ndarray (shape: (n,m) (default) or (m,n) (format: False))
'''
def csv_read(path: str, head = None, seperator = None, format = True):
    df = pd.read_csv(path, header=head, sep=seperator, engine='python')
    return df._values.transpose() if (format) else df._values

'''
# reads xlsx-file with pandas
#
# args:
# path : path to .csv file
# sheet : sheet-number or name in Excel-Document
# head : (default: None) 0, if the .csv-File has a Head for every col
# format - bool : decide, if the data should be transposed or not (default: True)
#
# returns:
# numpy.ndarray (shape: (n,m) (default) or (m,n) (format: False))
'''
def xlsx_read(path: str, sheet = 0, head = None, format=True):
    df = pd.read_excel(path, header=head, sheet_name = sheet)
    return df._values.transpose() if (format) else df._values