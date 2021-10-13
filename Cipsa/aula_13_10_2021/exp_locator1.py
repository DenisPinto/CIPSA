from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geocipsa")
cities = ['Barcelona','Madrid','London','Paris','Belem','Israel','Belém','Macapá']
for c in cities:
  coord = geolocator.geocode (c)
  print(coord.latitude, coord.longitude, c)