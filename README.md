# wig_splitters

**Overview**

This script will print a message to cs go chat every time you get a headshot. This program only works in game modes with rounds. 

This script utilizes Counter Strike's "Game State Integration" a method of triggering external systems from in-game events by sending packets of data to a given endpoint. To read more about Game State Integration visit the official Valve page https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration. 

While this script uses 
Game State Integration for a small purpose, Game State Integration is used in tournaments as a means of controlling physical elements of the tournament such as sounds, and stage lighting. I made this script as a fun project my friends and I could use during a time when we were playing a lot of Counter-Strike

Install instructions are targetted at a user who has little to no experience working with python or Counter-Strike game files.


**Install Instructions (no python installed)** * *Recommened* *

**All necessary files are included in wigs_plitters.zip**

1. Download wig_splitters.zip and extract to the desired install directory
2. Open wig_splitters that was extracted from wig_splitters.zip
3. Find gamestate_integration_wigsplitters.cfg and place it in your CSGO config folder 
(C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg\
4. In the wig_splitters directory open name.txt and enter your steam name on the first line then save
5. In CSGO open console (~) and bind "p" to the phrase to be printed to chat (bind p "say wig split")
6. Run wigsplitters.exe or wigsplitters.exe - Shortcut to run the program

**Install Instructions (with Python installed)**

1. Do steps 2 - 5 of Install Instructions no python installed
2. Install flask via "pip install flask" in cmd
3. Install keyboard via "pip install keyboard" in cmd
4. Run wig_splitters.py 

**To autorun with CSGO**

1. Create a new file on your name it "CSGO.bat"
2. Right-click > edit
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
