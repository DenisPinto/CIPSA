!pip install geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geocipsa")
cities = ['Barcelona','Madrid','London','Paris']
for c in cities:
  coord = geolocator.geocode (c)
  print(coord.latitude, coord.longitude, c)
