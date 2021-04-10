#!/usr/bin/env python3
from utils import mkpath
from os import listdir
from json import dump

def createjson(path, content):
    with open(path,"w") as file:
        dump(content, file, indent=4)

def createtext(path, content):
    with open(path,"w") as file:
        file.write(content)

def makefolders():
    mkpath("out/datapack/data/milhaxcustommodel/functions/")
    mkpath("minecraft/tags/functions/","out/datapack/data/")

def makefiles():
    createjson("out/datapack/pack.mcmeta", {"pack":{"pack_format":6,"description":"Milhax auto-CustomModelData picker"}})
    createjson("out/datapack/data/minecraft/tags/functions/load.json", {"values":["milhaxcustommodel:start"]})
    createjson("out/datapack/data/minecraft/tags/functions/tick.json", {"values":["milhaxcustommodel:trigger_detection"]})
    createtext("out/datapack/data/milhaxcustommodel/functions/replace.mcfunction","scoreboard players reset @s mhx_design")
    createtext("out/datapack/data/milhaxcustommodel/functions/start.mcfunction","scoreboard objectives add mhx_design trigger")
    createtext("out/datapack/data/milhaxcustommodel/functions/trigger_detection.mcfunction","scoreboard players enable @a mhx_design\nexecute as @a[scores={mhx_design=1..}] at @s run function milhaxcustommodel:replace")
    createtext("out/datapack/data/milhaxcustommodel/functions/uninstall.mcfunction","scoreboard objectives remove mhx_design")

def fillreplace():
    start = """execute as @e[distance=..5,type=item,nbt={Item:{tag:{display:{Name:'{"text":\""""
    mid = """"}'}}}}] run data modify entity @s Item.tag.CustomModelData set value """
    with open("out/datapack/data/milhaxcustommodel/functions/replace.mcfunction","a") as file:
        for item in listdir("treated_input/"):
            for design in listdir("treated_input/" + item):
                file.write("\n"+start+design[5:-4].replace("'","\\'").replace('"','\\"')+mid+str(int(design[0:4])))

def makedatapack():
    makefolders()
    makefiles()
    fillreplace()
