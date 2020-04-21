import pandas as pd
import folium
data = pd.read_csv("Newdataset.txt")

lat = list(data['LAT'])
lon = list(data['LON'])
# print(type(lat[4]))
samples = list(data['TOTAL'])
positive = list(data['POS'])
negative = list(data['NEG'])
location = list(data['LOCATION'])

def color_generator(pos):
    if pos < 100:
        return "green"
    elif 100 <= pos <= 300:
        return "orange"
    elif 300 <= pos <= 700:
        return "lightred"
    else:
        return "darkred"

map = folium.Map(location = [22.00, 77.00],zoom_start = 5, tiles = "Stamen Terrain")

print("adf")
fg = folium.FeatureGroup(name = "India Covid Cases Statewise")
i = 0
# popup = folium.Popup(str("Total samples: " + str(ts)+ ". Total Negative : "+ str(n) + "Total Positive: " + str(p)), parse_html = True)
for lt, ln, lc, ts, p, n in zip(lat, lon, location, samples, positive, negative):
    #print(i)
    #print(type(lt))
    #print(type(ln))
    #i += 1
    s = str(lc)+ "\n" + "Total samples: " + str(ts)+ "\n" + "Negative : "+ str(n) +"\n" + "Total Positive: " + str(p)
    fg.add_child(folium.Marker(location = [lt, ln], popup = folium.Popup(str(s), parse_html = True), icon = folium.Icon(color = color_generator(p))))

map.add_child(fg)
map.save("IndiaMap.html")
                 
