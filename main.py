import os 
import sys 
import subprocess

from config import music_dirs,player_path
from core import get_closest
from util import get_arg_full, build_files_list


def play(file_path, player_path):
    subprocess.Popen([player_path, file_path])

def main() :
    name = get_arg_full()
    print("Input song name : ", name)
    music_list = build_files_list(music_dirs)

    targ_name, targ_path = get_closest(name, music_list)
    
    print("Most similiar song {} on path {}".format(targ_name, targ_path))
    # input("Press any key to play ...")
    play(targ_path, player_path)

main()

