import os
import numpy as np
import sys
import pandas as pd
import pandas as pd
import pickle
from scipy.spatial.distance import cdist
from scipy.spatial.distance import pdist
from tqdm import tqdm

#------------------------------------------------------------
if __name__ == '__main__':

	#Input arguments
	filename = sys.argv[1]
	mindistance = float(sys.argv[2])

	#Read Coordinates
	coords = pd.read_csv('../data/tmp/' + filename + '.csv')
	coords = coords.values

	#Run
	clusters = []
	coord = np.zeros((1,2))
	for i in tqdm(range(coords.shape[0])):
		coord[0,:] = coords[i,:]
		dis = cdist(coords,coord)
		cluster = np.where(dis < mindistance)[0]
		clusters.append(cluster)

	#Pickle
	X = {}
	X['clusters'] = clusters
	pickle.dump(X, open('../data/tmp/' + filename + '.p','wb'))


