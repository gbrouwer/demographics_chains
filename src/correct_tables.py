import os
import sys
import pandas as pd
import numpy as np

#----------------------------------------------------------------
if __name__ == '__main__':

	#Counties to keep
	counties = ['36005','36047','36061','36081','36085']

	#Read Block Group Header file
	tablename = '../data/acs/nyc_blockgroups_header.csv'
	header = pd.read_csv(tablename)

	#Read Tables names
	tablenames = []
	tablefiles = []
	with open('/Volumes/2TStorage/CSV/nyc_tables','r') as f:
		for line in f:
			elements = line.rstrip().split('_')
			tablefiles.append('/Volumes/2TStorage/CSV/nyc_blockgroups/' + elements[0] + '.csv')
			tablenames.append('_'.join(elements[1:]).lower())

	#Loop Through Files
	for i in range(len(tablefiles)):

		#Read Data
		data = pd.read_csv(tablefiles[i])

		#Replace Columns with full names
		newcolumns = []
		keepcolumns = []
		columns = data.columns
		for column in columns:
			subset = header[header['Short_Name'] == column]
			if (len(subset) == 0):
				newcolumns.append(column)
				keepcolumns.append(column)
			else:
				fullname = subset['Full_Name'].values[0]
				fullname = fullname.lower()
				fullname = fullname.replace(',',' ')
				fullname = fullname.replace(':',' ')
				fullname = fullname.replace('for the population','')
				fullname = fullname.replace(' -- (estimate)','')
				fullname = fullname.replace('  ',' ')
				fullname = fullname.replace(' ','_')
				if '(margin of error)' not in fullname:
					keepcolumns.append(column)
					newcolumns.append(fullname)

		#New GeoID Column and remove non NYC counties
		data['GEOID'] = data['GEOID'].str.slice(7,30)
		data['COUNTYFIPS'] = data['GEOID'].str.slice(0,5)
		countyfips = data['COUNTYFIPS'].values
		keeprows = []
		for f,fip in enumerate(countyfips):
			if fip in counties:
				keeprows.append(f)
		data = data.iloc[keeprows]
		data = data[keepcolumns]
		data.columns = newcolumns

		#Store
		savename = tablefiles[i].replace('.csv','_cleaned.csv')
		data.to_csv(savename,index=False)

		#Create CSVT file
		savename = tablefiles[i].replace('.csv','_cleaned  .csvt')
		with open(savename,'w') as f:
			for i in range(len(newcolumns)-1):
				if (i != 1):
					f.write('"Integer",')
				else:
					f.write('"String(11)",')
			f.write('"Integer"\n')


	#Read Tract Header file
	tablename = '../data/acs/nyc_tracts_header.csv'
	header = pd.read_csv(tablename)

	#Read Tables names
	tablenames = []
	tablefiles = []
	with open('/Volumes/2TStorage/CSV/nyc_tables','r') as f:
		for line in f:
			elements = line.rstrip().split('_')
			tablefiles.append('/Volumes/2TStorage/CSV/nyc_tracts/' + elements[0] + '.csv')
			tablenames.append('_'.join(elements[1:]).lower())

	#Loop Through Files
	for i in range(len(tablefiles)):

		#Read Data
		data = pd.read_csv(tablefiles[i])

		#Replace Columns with full names
		newcolumns = []
		keepcolumns = []
		columns = data.columns
		for column in columns:
			subset = header[header['Short_Name'] == column]
			if (len(subset) == 0):
				newcolumns.append(column)
				keepcolumns.append(column)
			else:
				fullname = subset['Full_Name'].values[0]
				fullname = fullname.lower()
				fullname = fullname.replace(',',' ')
				fullname = fullname.replace(':',' ')
				fullname = fullname.replace('for the population','')
				fullname = fullname.replace(' -- (estimate)','')
				fullname = fullname.replace('  ',' ')
				fullname = fullname.replace(' ','_')
				if '(margin of error)' not in fullname:
					keepcolumns.append(column)
					newcolumns.append(fullname)

		#New GeoID Column and remove non NYC counties
		data['GEOID'] = data['GEOID'].str.slice(7,30)
		data['COUNTYFIPS'] = data['GEOID'].str.slice(0,5)
		countyfips = data['COUNTYFIPS'].values
		keeprows = []
		for f,fip in enumerate(countyfips):
			if fip in counties:
				keeprows.append(f)
		data = data.iloc[keeprows]
		data = data[keepcolumns]
		data.columns = newcolumns

		#Store
		savename = tablefiles[i].replace('.csv','_cleaned.csv')
		data.to_csv(savename,index=False)

		#Create CSVT file
		savename = tablefiles[i].replace('.csv','_cleaned.csvt')
		with open(savename,'w') as f:
			for i in range(len(newcolumns)-1):
				if (i != 1):
					f.write('"Integer",')
				else:
					f.write('"String(11)",')
			f.write('"Integer"\n')

