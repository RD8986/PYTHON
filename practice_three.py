# PRACTICE 3
# 1. Create a list of the first 10 odd numbers using list comprehension.
# 2. Create another list that contains the squares of these odd numbers.
# 3. Print both lists.

oddnumbers=[i for i in range(1,20,2)]
print(oddnumbers)
squareodd=[i**2 for i in oddnumbers]
print(squareodd)