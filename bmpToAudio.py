import os

### config
frames = 3257
#####
oss = "windows"
minFreq = 300
maxFreq = 20000
mode = "n"
sampleRate = 44100
pps = 100
# height = 365
# width = 1001
###
num = 0
num2 = 0

while True:
    # print(num)
    # num += 1
    if num == frames:
        break
    os.system(f".\\ARSS\\{oss}\\arss.exe .\\frames\\frame{num}.bmp -o .\\audio\\audio{num2}.wav -{mode} -min {minFreq} -max {maxFreq} -r {sampleRate} -p {pps} -q")
    print(num)
    num += 1
    num2 +=1

