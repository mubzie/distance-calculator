import inquirer
from geopy import distance
from geopy.geocoders import Nominatim
from geopy.point import Point
from simple_chalk import green, blue, yellow, red 



# Get user input for both first and second cities
first_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the first city"),
    inquirer.Text('country', message="what is the name of the first country")
])

# second_city = inquirer.prompt([
#     inquirer.Text('city', message="what is the name of the second city"),
#     inquirer.Text('country', message="what is the name of the second country")
# ])

# Initialize the geopy Nominatim module
geolocator = Nominatim(user_agent='distance calculator')

# Get first city latitude and longitude
first_loc_lat = geolocator.geocode(first_city).latitude
first_loc_lon = geolocator.geocode(first_city).longitude

# Get the point between the lat and lon
first_loc_point = Point(first_loc_lat, first_loc_lon)

# print(blue(first_location.raw))
print(green(first_loc_lat))
print(yellow(first_loc_lon))
print(red(first_loc_point))




# print(f'first location is {first_city}, {first_country}')
# print('the first city is {}, and the first country is {}'.format(questions))
# print(questions)


