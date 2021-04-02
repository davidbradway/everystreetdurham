import os
import glob

from everysinglestreet import Ride, Map

'''
 Call this script from the directory above `data`
 python src\everysinglestreet.py
'''

my_map = Map()

# read in municipal boundary
durham = 'data/geo/durham_boundary.json'
my_map.add_city_boundary(durham)

# all GPX files of my city runs are stored in the data/citystrides folder
# read in all GPX files and create a Ride() for each one
gpx_files = glob.glob(r'data\citystrides\*.gpx')

for filename in gpx_files:
    try:
	    my_ride = Ride(filename)
    	my_map.add_ride_gps_to_map(my_ride)
	except:
		pass

my_map.save_to_html('index.html')
