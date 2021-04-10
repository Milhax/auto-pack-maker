#!/usr/bin/env python3
from os import listdir
from shutil import move
from utils import trymake

def add_indexes():
    trymake('input/')
    trymake('treated_input/')
    for item in listdir("input"):
        trymake('treated_input/' + item)
        currnum = len(listdir('treated_input/' + item))
        for design in listdir("input/"+item):
            currnum+=1
            move("input/" + item + "/" + design , "treated_input/" + item + "/" + str(currnum).zfill(4) + '_' + design)
