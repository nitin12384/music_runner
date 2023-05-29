# List of directories
music_dirs = [r"C:\Users\nitin\Music\Tracks",r"C:\Users\nitin\Music\The great Ones",
r"C:\Users\nitin\Music\The great Ones\Sidetracked"]

player_path = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
# C:\Users\nitin\Music\Tracks\Alone.mp3
# sb.run([r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe", r"C:\Users\nitin\Music\Tracks\Alone.mp3"])

dm = False

import os 
import sys 
import subprocess

path_seperator = "\\" 

def get_name():
    nargs = len(sys.argv)
    assert nargs>=2 , "Give the name for music file"
    name = ""
    for i in range(1, nargs):
        name += sys.argv[i]
    return name


# Todo - Maybe generalize this
def remove_extension(filename : str) -> str :
    return filename[0:-4]

# return a list of tuples
def build_list():
    music_list = []
    for dir in music_dirs :
        music_list +=[ (remove_extension(cur), dir + path_seperator + cur) for cur in os.listdir(dir)]
        
    return music_list

def reduction(s:str)->str:
    # remove space, keep case small
    res = ""
    for c in s :
        if c.isalpha():
            res += c.lower()
        elif c.isdigit():
            res += c 

    return res

def edit_dist(a:str, b:str):
    na,nb = len(a), len(b)

    dp = [ [ 0 for i in range(nb+1)] for j in range(na+1)]

    # convert a -> b

    # for dp[0][j] and dp[i][0]
    for i in range(1,na+1):
        dp[i][0] = i 
    for j in range(1,nb+1):
        dp[0][j] = j

    for i in range(na):
        for j in range(nb):
            if a[i] == b[j] : 
                dp[i+1][j+1] = dp[i][j] 
            else :
                dp[i+1][j+1] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i][j])

    if dm :
        print(a, b, " : edit dist = ", dp[na][nb])

    return dp[na][nb] 


# Todo more generalize ?
# between 0 to 1
def name_difference(a : str, b : str) -> float :
    diff = edit_dist(reduction(a), reduction(b))
    if dm :
        print(a, b, " : diff = ", diff)
    return diff
    

def get_closest(name, music_list):
    min_dist = 1000000000
    targ_name = ""
    targ_path = ""
    for cur_name, path in music_list :
        dist = name_difference(name, cur_name)
        if dist < min_dist :
            targ_name = cur_name 
            targ_path = path 
            min_dist = dist

    if dm : 
        print("min_dist, name and path", min_dist, targ_name, targ_path)

    return targ_name, targ_path


def play(file_path, player_path):
    subprocess.run([player_path, file_path])

def main() :
    name = get_name()
    print("Input song name : ", name)
    music_list = build_list()

    targ_name, targ_path = get_closest(name, music_list)
    
    print("Most similiar song {} on path {}".format(targ_name, targ_path))
    play(targ_path, player_path)

main()

