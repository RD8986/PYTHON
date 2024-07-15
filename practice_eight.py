# PRACTICE EIGHT
# 1. Create a set of the first five prime numbers.
# 2. Add the number 11 to the set.
# 3. Remove the number 2 from the set.
# 4. Check if the number 7 is in the set.
# 5. Print the final set.


primenumbers = {2, 3, 5, 7, 11}
print(primenumbers)
primenumbers.add(11)
print("After adding 11, Result : ", primenumbers)
primenumbers.remove(2)
print("After removing 2, Result : ", primenumbers)
if 7 in primenumbers:
    print("Number 7 is in the set.")
else:
    print("Number 7 is not in the set.")

print("Final set of prime numbers:", primenumbers)
