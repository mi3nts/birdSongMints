# Introduction
In this repository the firmwareNow contains a Python script built on BirdNET (https://github.com/kahst/BirdNET-Analyzer) which can identify birds based on their sound.

## Action Items.
 - Give a small summary of whats been done on this doc. 
 - Acknowlege the original authers of the ML alg on this doc.
 - Create an ordered dictionary for each data point of data collected :
 ```
 def BSM001Write():
    # record datetime, label index and confidence
    sensorName = "BSM001"
    sensorDictionary = OrderedDict([
            ("dateTime"    , str(dateTime)),
            ("label "      , labelIndex),
            ("confidence " , confidenceIn),
                        ])    
        sensorFinisher(dateTime,sensorName,sensorDictionary)  
 
 ```
 - Time stamps should have just the starting time stamp of the given birdcall - So you can ignore the start time variable
 - Some means to keep the data if needed 
 - The Sample audio file should be saved as /home/teamlary/mintsData/tmp/ 
 - If at any case  you a saving the audio file it should be saved at /home/teamlary/mintsData/raw/yyyy/mm/dd/audio/MINTS_NODEID_BSM001_yyyy_mm_dd_hh_mm_ss.wav
format. 
- whole lot more commenting for the whole code


 

## Setup for Virtual Environment on Ubuntu 

  ```
  sudo apt-get install python3-venv
  python3 -m venv birdSongs
  source birdSongs/bin/activate
  sudo apt-get install build-essential libssl-dev libffi-dev python-dev
  pip3 install sounddevice
  pip3 install scipy
  pip3 install -U pip setuptools
  pip3  install pandas
  pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
  sudo apt-get install llvm-10 lldb-10 llvm-10-dev libllvm10 llvm-10-runtime
  sudo update-alternatives --install /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-10 10
  sudo update-alternatives --config llvm-config
  pip3 install llvmlite==0.35.0
  pip3 install librosa==0.9.1
  # Added on June 27 2022
  pip3 install pyserial
  pip3 install paho-mqtt
  pip3 install pyyaml==5.4.1
  pip3 install getmac
  pip3 install pynmea2
  pip3 install netifaces
  
  ```
