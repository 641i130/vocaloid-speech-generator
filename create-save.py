""" 
  _   _           _                    
 | \ | |   ___   | |_    ___   ___   _ 
 |  \| |  / _ \  | __|  / _ \ / __| (_)
 | |\  | | (_) | | |_  |  __/ \__ \  _ 
 |_| \_|  \___/   \__|  \___| |___/ (_)

There are two possible ways we could go about solving this problem.

We could make the user input a vpr file for the program to extract, edit then change 
   ___    _  __ 
  / _ \  | -___|
 | (_) | | |   
  \___/  |_|   
               
We could get the program to create its own json file then compress it into its own folder, naming it as a .vpr file.

The next problem would be to figure out how to make a monotone string of syllables into a realistic string of audio. Which would be easiest with ai.

"""
# First you need to generate a json file. 
# Then put it into a folder named Project.
# Next you would add the contents to it that generates the speech.
# Lastly you would compress the file and name the zip file as a .vpr file. This process is for Vocaloid 5

""" Example of a note or syllable for Vocaloid 5
"""
"""
{
"lyric": "st",
"phoneme": "a",
"isProtected": false,
"pos": 1920,
"duration": 960,
"number": 62,
"velocity": 64,
"exp": {"opening": 127},
"singingSkill": {
    "duration": 316,
    "weight": {
        "pre": 64,
        "post": 64
    }
},
"vibrato": {
    "type": 0,
    "duration": 0
}
},
"""

import json
from zipfile import ZipFile


file = "test.vpr"

f = codecs.open(file, 'rb', '')
readfile = f.readlines()
python(readfile)
"""
f.close()
print(json.dumps(readfile.json()))
"""
