# python_AtlasOEM_lib
Library for the Atlas Scientific OEM circuits

# Warning:
The pi 3 has problems communicating with the OEM circuits due to a clock stretching bug in the raspberry Pi hardware https://github.com/raspberrypi/linux/issues/4884
It is also an issue with the pi 4, but not always. 

In addition, recent Raspbery Pi OS updates (into Bullseye) have a glitch where bytes get dropped for reasons we cannot figure out, which seems distinct from the clock stretching bug. The last image that doesn't seem to have these issues is [this one](https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2021-05-28/), though updates may break it. 

You are welcome to try other distros or let us know if you figure out how to resolve this. 
