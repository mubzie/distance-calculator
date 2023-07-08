import inquirer
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from geopy.point import Point
from simple_chalk import green, blue, yellow, red 



# Get user input for first city and country
first_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the first city"),
    inquirer.Text('country', message="what is the name of the first country")
])

# Get user input for second city and country
second_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the second city"),
    inquirer.Text('country', message="what is the name of the second country")
])

# Initialize the geopy Nominatim module
geolocator = Nominatim(user_agent='distance calculator')

# Get first city latitude and longitude
first_loc_lat = geolocator.geocode(first_city).latitude
first_loc_lon = geolocator.geocode(first_city).longitude

# Get the point between the lat and lon
first_loc_point = Point(first_loc_lat, first_loc_lon)


print(green(first_loc_lat))
print(yellow(first_loc_lon))
print(red(first_loc_point))

# Get second city latitude and longitude
second_loc_lat = geolocator.geocode(second_city).latitude
second_loc_lon = geolocator.geocode(second_city).longitude

# Get the point between the two cities
second_loc_point = Point(second_loc_lat, second_loc_lon)


print(green(second_loc_lat))
print(yellow(second_loc_lon))
print(red(second_loc_point))


# Calculate the distance between the two cities
distance = geodesic(first_loc_point, second_loc_point).kilometers

# Calculating various distance for walking, bus, airplan, train, bicycle
walking = distance / 5
bus = distance / 60
airplane = distance / 800
train = distance / 400
bicycle = distance / 20

# All transporation Emojis
trans_emoji = {
    walking: '🚶‍♂️', 
    bicycle: '🚲', 
    bus: '🚌', 
    train: '🚆', 
    airplane: '✈️ '
    }


print(green('\nResults:'))
print(f'Distance between {first_city["city"]}, {first_city["country"]} and {second_city["city"]}, {second_city["country"]} by')
print(yellow(f'{trans_emoji[walking]} Walking: {distance:.2f} Km, Time: {walking:.2f} hours'))
print(yellow(f'{trans_emoji[bicycle]} Bicycle: {distance:.2f} Km, Time: {bicycle:.2f} hours'))
print(yellow(f'{trans_emoji[bus]} Bus: {distance:.2f} Km, Time: {bus:.2f} hours'))
print(yellow(f'{trans_emoji[train]} Train: {distance:.2f} Km, Time: {train:.2f} hours'))
print(yellow(f'{trans_emoji[airplane]} Airplane: {distance:.2f} Km, Time: {airplane:.2f} hours'))


