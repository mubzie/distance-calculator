import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, yellow, red 



# Get user input for both first and second cities
first_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the first city"),
    inquirer.Text('country', message="what is the name of the first country")
])

second_city = inquirer.prompt([
    inquirer.Text('city', message="what is the name of the second city"),
    inquirer.Text('country', message="what is the name of the second country")
])


print(first_city, second_city)




# print(f'first location is {first_city}, {first_country}')
# print('the first city is {}, and the first country is {}'.format(questions))
# print(questions)


