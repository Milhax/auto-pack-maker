#!/usr/bin/env python3
from os import listdir
from utils import mkpath
from shutil import copyfile
from json import load, dump

def makemcmeta():
    with open("out/resourcepack/pack.mcmeta","w") as file:
        dump({"pack":{"pack_format":6,"description":"Made with Milhax's auto-CustomModelData tool"}}, file, indent=4)

def gettype(item):
    if (item + ".json") in listdir("assets/minecraft/models/item/"):
        return("item/")
    elif (item + ".json") in listdir("assets/minecraft/models/block/"):
        return("block/")
    else:
        return("invalid")

def makejsons(item):
    type = gettype(item)
    out = "out/resourcepack/assets/minecraft/models/item/"+item+".json"
    copyfile("assets/minecraft/models/" + type +item+".json", out)
    with open(out, 'r') as file:
        data = load(file)

    data["overrides"] = []
    designs = sorted(listdir("treated_input/"+item))
    for i in range(len(designs)):
        design = designs[i][5:-4].replace(" ","_").replace("'","_").lower()
        data["overrides"].append({})
        data["overrides"][i]["predicate"] = {"custom_model_data" : int(designs[i][0:4])}
        data["overrides"][i]["model"] = "item/" + design

        with open("out/resourcepack/assets/minecraft/models/item/"+design+".json", 'w') as file:
            if (type == "item/"):
                dump({"parent": data["parent"],"textures":{"layer0":"items/"+design}}, file, indent=4)
            else:
                dump({"parent":"minecraft:item/handheld","textures":{"layer0":"items/"+design}}, file, indent=4)

    with open(out, 'w') as file:
        dump(data, file, indent=4)

def copypngs(item):
    for design in listdir("treated_input/"+item):
        copyfile("treated_input/"+item+"/"+design,
        "out/resourcepack/assets/minecraft/textures/items/"+design[5:].replace(" ","_").replace("'","_").lower())

def makeresource():
    mkpath("out/resourcepack/assets/minecraft/models/item/")
    mkpath("textures/items/", "out/resourcepack/assets/minecraft/")
    makemcmeta()
    for item in listdir("treated_input/"):
        makejsons(item)
        copypngs(item)
