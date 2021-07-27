# esp32cam
Experiments designed for the ESP32-Cam board.

## Install Micropython on the Board

Download the following binary to you worksation: https://github.com/lemariva/micropython-camera-driver/tree/master/firmware

Flash the image to the board following these instructions: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html


## Using the REPL on the Board

Install picocom and sz to handle serial communication and file transfer respectively

``sudo pacman -S picocom sz``

Connect to the board:

``sudo picocom /dev/tstyUSB0 -b115200``

Press enter to open the REPL.  Picocom has several commands to see them press **Ctrl-a** and then ***Ctrl-h***


## Compile Mircopython for Pinebook Pro (My dev env)

Compile Micropython for the Pinebook Pro so that you can develop locally.

Fork the micropython repo, check it out and create a new branch.

Install the build dependencies:

``
sudo pacman -S base-devel libffi zlib uzlib gzip arm-none-eabi-gcc arm-none-eabi-binutils arm-none-eabi-newlib ulab

``

This assumes gcc and gnu make are installed.

Follow the Micropython Readme.md instructions: https://github.com/micropython/micropython


**Note:** At some point I ran into a build error caused by python not finding a library. 
I created a build specific venv and installing the missing lib(s).

``
# IDK why huffman was missing...
pipenv install huffman
``


Assuming python is arleady installed and the shell starts with a catch all one activated, install ampy.

``pipenv install adafruit-ampy``

**Note:** Using picocom open a a REPL on the device and install all dependencies impoted into the python program using upip!

``import upip
upip.install('picoweb')``


From the  project working directory where the code is located run the following:
 
``sudo ampy --port /dev/ttyUSB0 run main.py``

Push the file to the board

``sudo ampy --port /dev/ttyUSB0 push main.py``


**Note:** I tried and tried to get picocom to write python files and this has been an exercise in futility.

