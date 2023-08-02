# Dictionary Comprehension in Python

# Dictionary comprehension is a concise way to create dictionaries using an expression. It can replace for loops and certain lambda functions.

# Syntax:
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

#---------------------------------------------------------------------------------------

# Example 1:
# We have a dictionary 'cities_in_F' representing temperatures in Fahrenheit for some cities.
# We use dictionary comprehension to convert these temperatures to Celsius and store them in 'cities_in_C' dictionary.

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

#---------------------------------------------------------------------------------------

# Example 2:
# We have a dictionary 'weather' representing the weather condition for some cities.
# We use dictionary comprehension to create a new dictionary 'sunny_weather' with only the cities having "sunny" weather.

weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

#---------------------------------------------------------------------------------------

# Example 3:
# We have a dictionary 'cities' representing temperatures in Fahrenheit for some cities.
# We use dictionary comprehension to categorize each city as "WARM" or "COLD" based on their temperature.

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
print(desc_cities)

#---------------------------------------------------------------------------------------

# Example 4:
# We define a function 'check_temp' that takes a temperature 'value' and returns the description "HOT", "WARM", or "COLD".
# We have a dictionary 'cities' representing temperatures in Fahrenheit for some cities.
# We use dictionary comprehension to categorize each city based on their temperature using the 'check_temp' function.

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)
