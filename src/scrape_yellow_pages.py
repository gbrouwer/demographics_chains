import os
import sys 
import pandas as pd 
import numpy as np
from tqdm import tqdm

#------------------------------------------------------------------
if __name__ == '__main__':

    #Restaurants query
    url = 'https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=New%20York%2C%20NY&page='

    #Loop
    for i in tqdm(range(100000)):
        outfile = '../data/restaurants/' + str(i+1) + '.html'
        thisurl = url + str(i+1)
        cmd = 'wget --quiet -O ' + outfile + ' ' + thisurl
        os.system(cmd)