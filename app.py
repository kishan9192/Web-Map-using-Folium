import pandas as pd
import folium
data = pd.read_csv("Volcanoes.txt")

# Fetching latitude and longitude from the data frame
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def color_generator(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation <= 3000:
        return 'orange'
    else:
        return 'red'
    
# Create an empty map
map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")
# map.save("Bright.html")

# Stockleaf Leaflet marker helps create
# the javascript and HTML code for the python map

feature_group = folium.FeatureGroup(name = "My Map")
# For loop for having multiple markers in the map

# Zip helps to iterate over two list at the same time
# lt 1 will get first item of lat, and ln 1 will get the first item of lon

# IF we want MARKERS USE THIS CODE
# for lt, ln, el in zip(lat, lon, elev):
#    feature_group.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(str(el), parse_html = True), icon = folium.Icon(color = color_generator(el))))

# IF WE WANT CIRCULAR MARKERS USE THIS CODE
for lt, ln, el in zip(lat, lon, elev):
    feature_group.add_child(folium.CircleMarker(location = [lt, ln], radius = 6, popup = folium.Popup(str(el), parse_html = True), fill_color = color_generator(el), color = 'grey', fill_opacity = 0.7))

#feature_group.add_child(folium.GeoJson(data = (open('world.json','r', encoding = 'utf-8-sig'))))

map.add_child(feature_group)
map.add_child(folium.LayerControl())
map.save("Bright.html")

