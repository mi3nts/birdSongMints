# birdSongMints
Contains firmware which classifies bird songs

## Central Node Intro 
### installing dependencies 
```install portaudio19-dev```

``` pip3 install PyAudio```
### installing udev rules
``` sudo nano /etc/udev/rules.d/93-mymic.rules```
### reloading
``` sudo udevadm control --reload```

