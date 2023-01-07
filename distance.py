# importing googlemaps module
import googlemaps

# Requires API key
gmaps = googlemaps.Client(key='')

# Requires cities name
my_dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]

# Printing the result
print(my_dist)












# importatnt link
# https://gist.github.com/olliefr/407c64413f61bd14e7af62fada6df866