import argparse
import os 
from collections import ChainMap

async def sum():
    # default values of first and second number
    deff = {'first': 0, 'second': 0}

    # adding argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--first', type=int)
    parser.add_argument('-y', '--second', type=int)
    
    # parssing the arguments
    arg = parser.parse_args()
    
    # making a dictionary from the arg
    cla = {key:value for key, value in vars(arg).items() if value} # vars(args) is equal to arg.__dict
    
    # create a ChainMap
    chain = ChainMap(cla,os.environ, deff)
    print(chain['first'] + chain['second'])

if __name__ == "__main__":
    sum()
