#!/usr/bin/env python3

#python imports
from os.path import expandvars
from platform import system
#custom imports
from copy_assets import jar_extract
from treat_in import add_indexes
from build_resourcepack import makeresource
from build_datapack import makedatapack

mcpath = ''

if (system() == 'Linux'):
    mcpath = expandvars('${HOME}/.minecraft/')
elif (system() == 'Windows'):
    mcpath = expandvars('${HOME}/Appdata\Roaming/.minecraft/')
elif (system() == 'Darwin'):
    mcpath = expandvars('${HOME}/Library/Application\\ Support/')

if (mcpath == ''):
    raise SystemExit("your system isn't currently supported... please tell me what you're running and where your mc folder is located ^^")

jar_extract(mcpath) #extracts models
add_indexes() #moves items from input to treated_input
makeresource() #generate resourcepack
makedatapack() #generate datapack
