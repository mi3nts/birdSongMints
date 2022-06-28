# Introduction
In this repository the firmwareNow contains a Python script built on BirdNET (https://github.com/kahst/BirdNET-Analyzer) which can identify birds based on their sound.

 

# Setup on Ubuntu 

Create a virtual environment with the name birdsongs and install the required packages. 

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
  ```
  ## Automate the code 
  Install the following packages to automate the code, recieve continous data and deal with the data through MQTT
  
  ```
  pip3 install pyserial
  pip3 install paho-mqtt
  pip3 install pyyaml==5.4.1
  pip3 install getmac
  pip3 install pynmea2
  pip3 install netifaces
  
  ```
