#!/usr/bin/env python3
from zipfile import ZipFile
from os.path import isdir
from os import listdir

def jar_extract(mcpath):
    if (isdir("assets/") == False):
        versions = listdir(mcpath + 'versions/')
        for i in range(len(versions)):
            print(i, ":", versions[i])
        try :
            v = int(input("which version we extracting boi "))
        except ValueError:
            raise SystemExit("invalid number")
        with ZipFile(mcpath + 'versions/' + versions[v] + "/" + versions[v] + ".jar") as file:
            for filename in file.namelist():
                if filename.startswith('assets/minecraft/models/'):
                    file.extract(filename)
