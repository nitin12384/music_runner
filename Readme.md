# Music Runner

A program to automatically play songs stored offline in the system based on approximate name matching.

# Requirements
Python 3

## Tested on 
Python 3.11.3
Windows 10 64-bit system

(Not tested on linux or any other system)

# Usage

Provide this information in the cofig.py file : 
- List of directories to search for music files.
- Path of the music player

Run main.py file and provide name of song as command line arguement.
Note - You dont need to use quotes while giving command line arguement, just give name as space seperated strings.
See the examples below .

# Matching Algorithm

# Usage Example and Screenshots

<img src='./screenshots/screenshot1.png'>
<img src='./screenshots/screenshot2.png'>
<img src='./screenshots/screenshot3.png'>

Configured alias using `cmder` tool to be able to use the program anywhere:
```
play_song=python "C:\Users\nitin\Programming\projects\music_runner\main.py" $*
```

As shown in the images, the program is usable from any directory.

<img src='./screenshots/screenshot4.png'>
<img src='./screenshots/screenshot5.png'>
