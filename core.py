
import math

from algo import edit_dist
from util import Logger
from util import string_reduction, split_to_alphanums
from config import dm

class Dist:
    def __init__(self):
        self.n_match = 0
        self.n_perf_match = 0
        self.n_inp_word = 0
        self.match_pos = []
        self.edit_dists = []
        self.tot_edit_dist = -1

    def __str__(self):
        return '[ n_match : ' + str(n_match) + ', n_perf_match : ' + str(n_perf_match) + \
        ', tot_edit_dist : ' + str(tot_edit_dist) + ']'
    
    def __lt__(self, obj):
        # return True iff self < obj
        # more perfect match, less distanc
        if self.n_perf_match != obj.n_perf_match :
            return self.n_perf_match > obj.n_perf_match
        
        # same n_perf_match
        if self.n_match != obj.n_perf :
            return self.n_match > obj.n_match 
        
        return self.tot_edit_dist < obj.tot_edit_dist


# a dummy infdist object
InfDist = Dist()

def word_closeness(inp_list : list, targ_list : list):
    ninp, ntarg = len(inp_list), len(targ_list)

    empty_list = [ -1 for i in range(ninp)]
    match_pos, edit_dists = empty_list, empty_list
    n_match = 0
    n_perf_match = 0
    dist_fraction_thresh=0.3
    

    for i in range(ninp):
        # find word[i] in targ
        
        # floor of ceil
        x_thresh = math.floor(dist_fraction_thresh*len(word[i]))
        minx, reqj = math.inf,-1
        for j in range(ntarg):
            x = edit_dist(inp_list[i], targ_list[j])
            if x < minx:
                minx,reqj = x,j
        if minx <= x_thresh :
            # match found
            match_pos[i], edit_dists[i] = reqj, minx
            n_match += 1
            if minx == 0 :
                n_perf_match += 1
    
    return n_match, n_perf_match, match_pos,edit_dists

def get_distance(inp, targ, inp_red, inp_list):
    targ_red = string_reduction(targ)
    targ_list = split_to_alphanums(targ)
    
    dist = Dist()
    dist.n_inp_word = len(inp_list)
    dist.n_match, dist.n_perf_match, dist.match_pos, dist.edit_dists = word_closeness(inp_list, targ_list)
    dist.tot_edit_dist = edit_dist(inp_red, targ_red)

    return dist

def get_closest(name, music_list):

    name_red = string_reduction(name)
    name_word_list = split_to_alphanums(name)

    min_dist = InfDist
    targ_name = ""
    targ_path = ""
    for cur_name, path in music_list :
        dist = get_distance(name, cur_name, name_red, name_word_list)
        if dist < min_dist :
            targ_name = cur_name 
            targ_path = path 
            min_dist = dist

    if dm : 
        print("min_dist, name and path", min_dist, targ_name, targ_path)

    return targ_name, targ_path
