#! /usr/bin/python3

# import
import yfinance as yf
from pathlib import Path

class TickerItem:
    def __init__(self, symbol, isin, name):
        self.symbol = symbol
        self.isin = isin
        self.name = name

def read_matrix(file_location):
    matrix = []
    # create file, if it not exists
    datafile = Path(file_location)
    datafile.touch(exist_ok=True)
    f = open(datafile)
    for line in f:
        # remove trailing newlines
        record = line.split("|")
        record[len(record) - 1] = record[len(record) - 1].rstrip()
        matrix.append(record)
    f.close()
    return matrix 

def write_matrix(matrix, file_location):
    f = open(file_location, "w")
    for line in matrix:
        f.write("|".join(line) + "\n")
    f.close()

def get_yahoo_ticker():
    symbol = input("Yahoo Finance Symbol: ")
    symbol = symbol.upper()
    ticker = yf.Ticker(symbol)
    if (ticker.info["logo_url"] != ""):
        return TickerItem(symbol, ticker.isin, ticker.info["shortName"])
    else:
        return None

def symbol_exists(symbol, matrix):
    for item in matrix:
        if (item[0] == symbol):
            return True
    return False

def get_datetime_array(date_string):
    dt_array = []
    dt_array.append(date_string[0:4])
    dt_array.append(date_string[5:7])
    dt_array.append(date_string[8:10])
    dt_array.append(date_string[11:13])
    dt_array.append(date_string[14:16])
    dt_array.append(date_string[17:19])
    return dt_array
