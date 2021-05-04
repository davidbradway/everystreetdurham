import glob
import sys

sys.path.append('everysinglestreet')
from src.everysinglestreet import Ride, Map
import datetime

'''
 Call this script from the directory above `data`
 python everysinglestreet.py
'''

# Find the total distance run in the city since starting the #everysinglestreet challenge in earnest
date = '2019-10-30'
city_strides_start_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
dist_cs = 0
runs_cs = 0

dist_all= 0
runs_all = 0

my_map = Map(lat=35.99, lon=-78.90, zoom=12, tiles='Stamen Toner')

# read in municipal boundary
durham = 'data/geo/durham_boundary.json'
my_map.add_city_boundary(durham)

    # all GPX files of my city runs are stored in the data\citystrides folder
# GPX files of reduced complexity are stored in the data\reduced folder
# read in all GPX files and create a Ride() for each one
gpx_files = glob.glob(r'data\reduced\*.gpx')

for filename in gpx_files:
    try:
        my_ride = Ride(filename)
        my_map.add_ride_gps_to_map(my_ride)
        if my_ride.ride_date.date() > city_strides_start_date:
            dist_cs += my_ride.ride_length_miles
            runs_cs += 1
        dist_all += my_ride.ride_length_miles
        runs_all += 1

    except Exception as e:
        print(e)

my_map.save_to_html(r'docs\index.html')

print(f'dist_cs= {dist_cs}')
print(f'runs_cs= {runs_cs}')

print(f'dist_all= {dist_all}')
print(f'runs_all= {runs_all}')
