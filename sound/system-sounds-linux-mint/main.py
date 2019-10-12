
# date: 2019.09.15
# 

import os
import sounddevice as sd
import soundfile as sf

directory = '/usr/share/sounds/LinuxMint/stereo/'

for filename in os.listdir(directory):
    #if 'dialog' in filename:
    print(filename)
    path = os.path.join(directory, filename)
    data, sr = sf.read(path)
    sd.play(data, sr)
    sd.wait()


