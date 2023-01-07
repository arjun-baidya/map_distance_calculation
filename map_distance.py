from geopy.geocoders import Nominatim
from geopy import distance

geocoder = Nominatim(user_agent="arjun")

location1 = str(input("from  ",  ))
location2 = str(input("To"))

print("geocoder", geocoder)

cordinate1 = geocoder.geocode(location1)
cordinate2 = geocoder.geocode(location2)
print("cordinates1", cordinate1)

lat1, long1 = (cordinate1.latitude),(cordinate1.longitude)
print("latitude1", lat1, long1)
lat2, long2 = (cordinate2.latitude),(cordinate2.longitude)
print("latitude1", lat2, long2)


place1 = (lat1,long1)
place2 = (lat2, long2)

print("distance :", distance.distance(place1,place2))
