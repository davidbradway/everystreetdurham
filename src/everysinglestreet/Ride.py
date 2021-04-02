import gpxpy

class Ride:
    def __init__(self, filename):
        self._gpx = gpxpy.parse(open(filename, 'r'))
        self.ride_date = self._gpx.time
        self.filename = filename
        self.gps_points = self.parse_gpx_file()
        self.ride_length_meters = self._gpx.length_2d()
        self.ride_length_miles = self.ride_length_meters * 0.000621371

    def parse_gpx_file(self):
        """Method for parsing GPX file into list of points needed for mapping"""
        points = []
        for track in self._gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        
        return points