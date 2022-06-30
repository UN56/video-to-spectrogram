# import numpy as np
from ast import Lambda
from pydub import AudioSegment
import functools

## how many audio File (example 10 file, put 11)
audioNum = 5
##
audioNumStart = 0
num = 0
output = []

for i in range(audioNumStart, audioNum):
    # output.append(AudioSegment.from_wav(f".\\audio\\audio{i}.wav"))
    # output.append(AudioSegment.from_mp3("delay1.mp3"))
    output.append(AudioSegment.from_mp3(f".\\audioOutput\\output{i}.mp3"))
    print(i)
        # audioNumStart += 1
    
    # flatten_list = list(np.concatenate(output). flat)
    # join = "".join([object(x) for x in output])
joinn = functools.reduce(lambda a, b: a+b, output)

joinn.export("audioOutput\\output.mp3", format="mp3")