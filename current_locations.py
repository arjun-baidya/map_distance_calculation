import geocoder
import folium
import requests

ip = geocoder.ip('me')
myAddress = ip.latlng
print("myAddress", myAddress)
# my_add = ' '.join(myAddress)

my_map = folium.Map(location=myAddress, zoom_start=12)
folium.CircleMarker(location=myAddress,radius=50, popup='Yorkshire').add_to(my_map)
folium.Marker(myAddress,popup='Yorkshire').add_to(my_map)
print("my map", my_map)
my_map.save('my_map.html')
