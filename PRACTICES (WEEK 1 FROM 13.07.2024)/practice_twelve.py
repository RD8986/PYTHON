# PRACTICE 12
# • Create a dictionary where each key is a country and the value is another dictionary
#   with keys "capital" and "population".
# • Access and print the capital of one country.
# • Update the population of another country.
# • Print the final dictionary.

countries = {
    "USA": {"capital": "Washington D.C.", "population": 331449281},
    "China": {"capital": "Beijing", "population": 1444216107},
    "India": {"capital": "New Delhi", "population": 1393409038}
}
print("\n Three Countries capital and thier population : ")
print(countries)

print("\n Capital of China : ")
print(countries["China"]["capital"])

countries["India"]["population"] = 1393409039
print("After updating India population : ")
print(countries)
