
# return the arg as string
def get_arg_full():
    nargs = len(sys.argv)
    assert nargs>=2 , "Give the name for music file"
    res = ""
    for arg in sys.argv[1:] :
        res += arg


# Todo - Maybe generalize this
def remove_filename_extension(filename : str) -> str :
    return filename[0:-4]


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
        file_list +=[ (remove_extension(cur), dir + path_seperator + cur) for cur in os.listdir(dir)]
        
    return file_list
