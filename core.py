
class Dist:
    def __init__(self):
        self.word
    

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
