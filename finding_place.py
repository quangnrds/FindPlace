# Finding interesting place
# This scripts helps to make a wish lists and displaying the marked location in OpenStreetMap 

API_KEY='Put your googlemaps api here'
import requests
import json
import folium
import webbrowser, os
import datetime

s = input("Place name: ")
n = nom.geocode(s.lower())

# getting location info
HN_coffee=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}, {}&radius=1000&type= cafe, coffee &keyword= Highland, cafe, coffee &key={}'.format(n.latitude, n.longitude, API_KEY)).json()
HL_add =[(i['name'], i['vicinity'],i['rating']) for i in HN_coffee['results']]

# generating lat,lon
lat =[i['geometry']['location']['lat'] for i in HN_coffee['results']]
lon =[i['geometry']['location']['lng'] for i in HN_coffee['results']]

# creat map via folium
map_cf = folium.Map(location=[21.5, 105.3], zoom_start=10, tiles="Mapbox Bright")
fghl = folium.FeatureGroup(name='Highland Coffee Map')

# making list of the location
for lt, ln in zip(lat,lon):
    fghl.add_child(folium.CircleMarker(location=[lt,ln], radius=6,popup="Coffee", fill_color = 'red', fill = True, color='grey', fill_opacity=0.7)) 
    #map_cf = folium.Map(location=[lt,ln], zoom_start=10, tiles="Mapbox Bright")
# outcome    
today = datetime.date.today()
map_cf.add_child(fghl)
map_cf.save("/path_to_file/name.html")
#print('Coordinates "{}": {}, {} '.format(s.capitalize(), n.latitude, n.longitude))
cf_li =  [(i,j) for i,j in enumerate(HL_add, start=1)]
#print(cf_li)
webbrowser.open('file://'+os.path.realpath("/path_to_file/name.html"))
print("** Path result lists : '/path_to_file/name.txt'")
with open ("/path_to_file/name.txt".format(str(today)), "w") as f:
    for i in cf_li:
        f.write(''.join('%s %s\n'%i))
