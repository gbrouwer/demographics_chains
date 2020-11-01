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
	filename = 'nyc_boroughs'
	mindistance = float(sys.argv[1])

	#Read Coordinates
	coordsdf = pd.read_csv('../data/tmp/' + filename + '.csv')
	coords = coordsdf[['lat','lng']].values
	borocodes = coordsdf['borocode'].values

	#Run
	clusters = []
	coord = np.zeros((1,2))
	for i in tqdm(range(coords.shape[0])):
		coord[0,:] = coords[i,:]
		thisboro = borocodes[i]
		indices = np.where(borocodes != thisboro)[0]
		dis = cdist(coords[indices,:],coord)
		cluster = np.where(dis < mindistance)[0]
		if (len(cluster) > 1):
			cluster = indices[cluster]
			clusters.append(cluster)

	#Pickle
	X = {}
	X['clusters'] = clusters
	pickle.dump(X, open('../data/tmp/' + filename + '.p','wb'))


