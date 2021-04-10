#!/usr/bin/env python3
from os import mkdir

def trymake(path):
        try:
            mkdir(path)
        except FileExistsError:
            pass

def mkpath(path, inDir=""):
    steps = path.split("/")
    for i in range(1,len(steps)):
        b = ''
        for j in range(i):
            b += steps[j] + "/"
        b = inDir + b
        trymake(b)
