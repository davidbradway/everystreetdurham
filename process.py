import os
from shutil import copy
import gpxpy
import gpxpy.gpx
import pickle

'''
 This script copies GPX files that meet certain criteria, like sport type and location
 It keeps the originals to maintain easy incremental backups
'''

def close_to_city(point, city_latitude=35.994034, city_longitude=-78.898621, thresh = 0.2):
    # https://www.usgs.gov/faqs/how-much-distance-does-a-degree-minute-and-second-cover-your-maps?qt-news_science_products=0#qt-news_science_products
    # about 10 miles in any direction
    return abs(point.latitude - city_latitude) < thresh and abs(point.longitude - city_longitude) < thresh


def main(directory = 'garminactivities', keepdirectory = 'citystrides'):
    files = os.listdir(os.path.join('data', directory))

    # use local pickle cache file to avoid rechecking
    if os.path.exists('.checked.pkl'):
        with open('.checked.pkl', 'rb') as f:
            checked = pickle.load(f)
        print("Cache loaded, ", end="")
    else:
        checked = []

    for filename in files:
        if filename not in checked:
            try:
                if not os.path.exists(os.path.join('data', keepdirectory, filename)) and filename.endswith(".gpx"):
                    with open(os.path.join('data', directory, filename), 'r') as f_in:
                        gpx = gpxpy.parse(f_in)

                    # there may not be any tracks - exception
                    track = gpx.tracks[0]

                    if 'run' in track.type or 'walk' in track.type or 'other' in track.type:
                        segment = track.segments[0]
                        point = segment.points[0]

                        if close_to_city(point):
                            print(f"{filename} \t {track.type} in City. Copy")
                            copy(os.path.join('data', directory, filename), os.path.join('data', keepdirectory, filename))
            except Exception as e: # work on python 3.x
                # print(str(e))
                pass

    checked = files
    with open('.checked.pkl', 'wb') as f:
        pickle.dump(checked, f)
    print("saved.")


if __name__ == '__main__':
    main()
