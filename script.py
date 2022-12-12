import webbrowser
import openrouteservice as ors
import folium
import pandas as pd
import random
import sys

try:
    localRunning = (sys.argv[1] == "local")
except IndexError:
    localRunning = False

r = lambda: random.randint(0,255)

if (localRunning):
    client = ors.Client(base_url='http://localhost:8080/ors')
else:
    client = ors.Client(key='5b3ce3597851110001cf624899eccde98e66451c83af703f76b754ff')

renderedMap = folium.Map(location=[41.87578707461336, 12.482115568674097], tiles='cartodbpositron', zoom_start=13)

data = pd.read_csv("./input.csv")

coordinates = []


latA = list(data["latA"])
lngA = list(data["lngA"])
latB = list(data["latB"])
lngB = list(data["lngB"])

distances=[]

fg = folium.FeatureGroup(name="Markers")
iterator=0
for latA, lngA, latB, lngB in zip(latA, lngA, latB, lngB):
    coordinates = []
    coordinates.append([lngA,latA])
    coordinates.append([lngB,latB])
    # aggiungi Marker sulla mappa
    fg.add_child(folium.Marker(location=[latA,lngA], popup=str(iterator) + '_Origin', icon=folium.Icon(color='blue')))
    fg.add_child(folium.Marker(location=[latB,lngB], popup=str(iterator) + '_Destination', icon=folium.Icon(color='red')))


    route = client.directions(
        coordinates=coordinates,
        profile='foot-walking',
        format='geojson',
        instructions='false',
        units="m",
        preference="shortest",
    )

    distances.append(route['features'][0]['properties']['summary']['distance'])

    color = '#%02X%02X%02X' % (r(),r(),r())

    #
    folium.PolyLine(
        locations=[list(reversed(coord)) 
            for coord in 
                route['features'][0]['geometry']['coordinates']], 
        popup="track n° " + str(iterator) + " \ndistanza= " + str(distances[iterator]) + " m", 
        color=color).add_to(renderedMap
    )
    route = {}
    iterator+=1
    
renderedMap.add_child(fg)
data.insert(4, "Distanza", distances,True)
data.index.name = "id"
data.to_csv('output.csv', index=True)

output_file = "map.html"
renderedMap.save(output_file)
webbrowser.open(output_file, new=2)
