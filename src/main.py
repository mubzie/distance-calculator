import inquirer
from geopy.geocoders import Nominatim
from geopy.point import Point
from geopy.distance import geodesic
from simple_chalk import green, blue, yellow, red 



# Get user input for first city and country
first_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the first city"),
    inquirer.Text('country', message="which country is the first city located")
])

# Get user input for second city and country
second_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the second city"),
    inquirer.Text('country', message="which country is the second city located")
])

# Initialize the geopy Nominatim module
geolocator = Nominatim(user_agent='distance calculator')

# Getting the first city latitude and longitude using the geopy Nominatim module
first_city_lat = geolocator.geocode(first_city).latitude
first_city_lon = geolocator.geocode(first_city).longitude

# Get the lat and lon point of the first city
first_loc_point = Point(first_city_lat, first_city_lon)

# Getting second city latitude and longitude using the geopy Nominatim module
second_loc_lat = geolocator.geocode(second_city).latitude
second_loc_lon = geolocator.geocode(second_city).longitude

# Get the lat and lon point of the second city
second_loc_point = Point(second_loc_lat, second_loc_lon)

# Get the distance between the two cities and return the result in kilometers
distance = geodesic(first_loc_point, second_loc_point).kilometers

# Calculating various distance for walking, bus, airplane, train, bicycle,
# using different measurement metric that correspond to each transportation mode
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

# printing out the result to the terminal
print(green('\nResults:'))
print(f'Distance between {first_city["city"]}, {first_city["country"]} and {second_city["city"]}, {second_city["country"]} by')
print('-----------------------------------------------------')
print(yellow(f'{trans_emoji[walking]} Walking: {distance:.2f} Km, Time(ETA): {walking:.2f} hours'))
print('-----------------------------------------------------')
print(yellow(f'{trans_emoji[bicycle]} Bicycle: {distance:.2f} Km, Time(ETA): {bicycle:.2f} hours'))
print('-----------------------------------------------------')
print(yellow(f'{trans_emoji[bus]} Bus: {distance:.2f} Km, Time(ETA): {bus:.2f} hours'))
print('-----------------------------------------------------')
print(yellow(f'{trans_emoji[train]} Train: {distance:.2f} Km, Time(ETA): {train:.2f} hours'))
print('-----------------------------------------------------')
print(yellow(f'{trans_emoji[airplane]} Airplane: {distance:.2f} Km, Time(ETA): {airplane:.2f} hours'))
print('-----------------------------------------------------')


