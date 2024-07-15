# PRACTICE 11
# • Create a dictionary with five key-value pairs representing different cities and their
#   populations.
# • Use the get method to access the population of a specific city.
# • Use the pop method to remove a city from the dictionary.
# • Print the final dictionary.

cities = {
    "Patna":  2633000,
    "Delhi":  33807000,
    "Mumbai": 21673000,
    "Hyderabad": 10534000,
    "Bangalore": 11993000
}
print(cities)

mycity = cities.get("Patna")
print("\n My city population : ", mycity)

removedcity = cities.pop("Bangalore")
print("\n After removing a city : ")
print(cities)
