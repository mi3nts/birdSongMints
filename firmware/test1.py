import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import time
import sys
from scipy.fftpack import fft
from matplotlib import style



FORMAT = pyaudio.paInt16 # We use 16bit format per sample
CHANNELS = 1
RATE =  44000
CHUNK = 1024 # 1024bytes of data red from a buffer
INTERVAL = 1/RATE
dev_index = 11

audio = pyaudio.PyAudio()

print("Hello")

print("Hello22")

for i in range(audio.get_device_count()):
  dev = audio.get_device_info_by_index(i)
  print((i,dev['name'],dev['maxInputChannels']))

# start Recording
stream = audio.open(format = FORMAT,rate = RATE,channels = CHANNELS, \
                    output = False,input = True, \
                    frames_per_buffer=CHUNK,input_device_index = dev_index)


def main():

    global keep_going
    keep_going = True

    stream.start_stream()

    startTime = time.time()
    while keep_going:
        try:
            stream.start_stream()
            yf = returnPowerSpectrum()
            maxInd = np.argmax(yf)
            xf = np.linspace(0.0, 1.0/(2.0*INTERVAL), CHUNK//2)
            print("=-----------")
            #print(yf)
            print(xf[maxInd])
            stream.stop_stream()
            plt.plot(xf,yf)
            plt.pause(0.00001)
            plt.clf()


        except KeyboardInterrupt:
            keep_going=False
        except:
            pass
    #
    # # Close up shop (currently not used because KeyboardInterrupt
    # is the only way to close)
    stream.stop_stream()
    stream.close()
    audio.terminate()


def returnPowerSpectrum():
    yf            = fft(np.fromstring(stream.read(CHUNK), np.int16))
    powerSpectrum = 2.0/CHUNK * np.abs(yf[0:CHUNK//2])
    return powerSpectrum




if __name__ == "__main__":
   main()
