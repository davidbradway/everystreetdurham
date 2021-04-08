import glob
import sys
sys.path.append('everysinglestreet')
from src.everysinglestreet import Ride, Map

'''
 Call this script from the directory above `data`
 python everysinglestreet.py
'''

my_map = Map(lat=35.99, lon=-78.90, zoom=12, tiles='Stamen Toner')

# read in municipal boundary
durham = 'data/geo/durham_boundary.json'
my_map.add_city_boundary(durham)

# all GPX files of my city runs are stored in the data/citystrides folder
# read in all GPX files and create a Ride() for each one
gpx_files = glob.glob(r'data\reduced\*.gpx')

for filename in gpx_files:
    try:
        my_ride = Ride(filename)
        my_map.add_ride_gps_to_map(my_ride)
    except:
        pass

my_map.save_to_html(r'docs\index.html')
