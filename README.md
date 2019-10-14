# wig_splitters

**Overview**

This program will print a message to cs go chat everytime you get a headshot. This program only works in gamemodes with rounds.

**Install Instructions (no python installed)** * *Recommened* *

**All necissary files are included in wigs_plitters.zip**

1. Download wig_splitters.zip and extract to desired install directory
2. Open wig_splitters that was extracted from wig_splitters.zip
3. Find gamestate_integration_wigsplitters.cfg and place it in your csgo config folder 
(C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\
4. In the wig_splitters directory open name.txt and enter your steam name on the first line then save
5. In csgo open console (~) and bind "p" to the phrase to be printed to chat (bind p "say wig split")
6. Run wigsplitters.exe or wigsplitters.exe - Shortcut to run the program

**Install Instuctions (with python installed)**

1. Do steps 2 - 5 of Install Instructions no python installed
2. Install flask via "pip install flask" in cmd
3. Install keyboard via "pip install keyboard" in cmd
4. Run wig_splitters.py 

**To auto run with csgo**

1. Create a newfile on your name it "CSGO.bat"
2. Right click > edit
3. type:

START steam://rungameid/730

"your wig_splitters.exe path" 

ex:

START steam://rungameid/730

"C:\Users\user\OneDrive\Desktop\wig_splitters" 

* *if python is installed:* 

START steam://rungameid/730

"python install dir" "wig_splitters.py dir" 


4. To change the icon create a shortcut to the CSGO.bat, download the csgo-icon included (csgoIcon.ico) and set it as the icon in properties.
