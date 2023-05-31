
from datetime import datetime
import sys
import os

from config import path_seperator

class Logger:
    @staticmethod
    def log(msg):
        # msg could be str or may not be ...
        print('[' + str(datetime.now()) + '] ' + msg)
    @staticmethod
    def info(msg):
        print('[' + str(datetime.now()) + '] ' + msg)

# return the arg as string
def get_arg_full():
    nargs = len(sys.argv)
    assert nargs>=2 , "Give the name for music file"
    res = ""
    for arg in sys.argv[1:] :
        res += arg + " "
    
    # remove last space
    res = res.rstrip()
    return res


# Todo - Maybe generalize this
def remove_filename_extension(filename : str) -> str :
    return filename[0:-4]

def split_to_alphanums(s:str)->list:
    n = len(s)
    wordlist = []
    word = ""
    for i in range(0,n):
        c = s[i]
        if c.isalpha() or c.isdigit() :
            if c.isalpha():
                c = c.lower()
            word += c
            if i == n-1 :
                wordlist.append(word)
        else :
            # if word is not empty
            if word != "" :
                wordlist.append(word)
            word = ""
    return wordlist
        

def string_reduction(s:str)->str:
    # remove space, keep case small
    res = ""
    for c in s :
        if c.isalpha():
            res += c.lower()
        elif c.isdigit():
            res += c 

    return res


# return a list of tuples
def build_files_list(dir_list):
    file_list = []
    for dir in dir_list :
        file_list +=[ (remove_filename_extension(cur), dir + path_seperator + cur) for cur in os.listdir(dir)]
        
    return file_list
