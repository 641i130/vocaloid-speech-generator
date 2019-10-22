# This should be the main program that outputs the save.

import binascii
import json
import codecs

file = "test.vpr"

f = codecs.open(file, 'rb', '')
readfile = f.readlines()
python(readfile)
"""
f.close()
print(json.dumps(readfile.json()))
"""
