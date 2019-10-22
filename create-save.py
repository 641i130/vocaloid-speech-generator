# This should be the main program that outputs the save.

import binascii
import json
import codecs

# First you need to generate a json file. 
# Then put it into a folder named Project.
# Next you would add the contents to it that generates the speech.
# Lastly you would compress the file and name the zip file as a .vpr file. This process is for Vocaloid 5


file = "test.vpr"

f = codecs.open(file, 'rb', '')
readfile = f.readlines()
python(readfile)
"""
f.close()
print(json.dumps(readfile.json()))
"""
