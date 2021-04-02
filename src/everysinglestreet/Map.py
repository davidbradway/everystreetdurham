import random
import folium

class Map:
    """
    Class for creating a html map. If using in a Jupyter notebook this map can be 
    viewed by calling the map attribute. Otherwise, use the save_to_html() method
    """
    def __init__(self, lat=35.99, lon=-78.90, zoom=12, tiles='Stamen Toner'):
    # def __init__(self, lat=42.89, lon=-78.82, zoom=12, tiles='Stamen Toner'):
        self.map = folium.Map(location=[lat, lon], zoom_start=zoom, tiles=tiles)
        self._colors = [
                        '#d35400', '#e67e22', '#f39c12', '#f1c40f', '#2ecc71', 
                        '#27ae60', '#16a085', '#1abc9c', '#3498db', '#2980b9', 
                        '#8e44ad', '#9b59b6', '#e74c3c', '#c0392b'
                        ]

    def add_ride_gps_to_map(self, Ride):
        """Overlays GPS path of ride on map"""
        folium.PolyLine(Ride.gps_points,
                        color=random.choice(self._colors),
                        weight=4,
                        opacity=1, 
                        tooltip=f"{Ride.ride_length_miles:.1f} miles on {Ride.ride_date:%Y-%m-%d}"
                        ).add_to(self.map)

    def add_city_boundary(self, filename):
        """
        Overlays outline of city boundary on map. Recommended to do this first before adding
        rides so boundary is on the bottom most layer
        """
        style = {'fillOpacity': 0.2, 'color': 'black'}

        folium.GeoJson(
            filename,
            style_function=lambda x: style
        ).add_to(self.map)

    def save_to_html(self, filename):
        """Saves map to a html file to be viewed if not using Jupyter notebook. """
        self.map.save(filename)