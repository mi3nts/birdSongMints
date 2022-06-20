# birdSongMints
Contains firmware which classifies bird songs

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

**Try initially on testBedBirdCalls PC on your DW Service Account**

## Updates to the current system

- Install requirments.txt
- reboot 
- ``` pip3 install sounddevice==0.4.4```
- ``` pip3 install -U pip setuptools ```
- ``` pip3  install pandas ```
- ``` pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime ```
- 

## VENV 

  ```
  python3 -m venv birdSongs
  source birdSongs/bin/activate
  pip3 install sounddevice
  pip3 install scipy
  
  
  ```
