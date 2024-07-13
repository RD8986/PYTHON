# PRACTICE 7
# 1. Create a set of the first five odd numbers.
# 2. Create another set of the first five even numbers.
# 3. Find the union and intersection of these sets.
# 4. Print the results.

first_five_oddnumbers={1, 3, 5, 7, 9}
first_five_evennumbers={2, 4, 6, 8, 10}

union=first_five_oddnumbers.union(first_five_evennumbers)
intersection=first_five_oddnumbers.intersection(first_five_evennumbers)
print("\n Union of first five odd & even numbers : ")
print(union)
print("\n Intersection of first five odd & even numbers : ")
print(intersection)