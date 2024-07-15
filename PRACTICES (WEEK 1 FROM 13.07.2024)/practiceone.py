#PRACTICE 1 
# 1. Create a list of the first 10 square numbers.
#    Example: square number means [1,4,9,……..]
# 2. Replace the third element with 50.
# 3. Insert a new element 25 at the fifth position.
# 4. Remove the last element from the list.
# 5. Print the final list.

square=[]
for i in range(1,11):
    square.append(i**2) 
print("Squares of 1 to 10 : ")
print(square)
square[2]=50
print("\n After Replacing third element with 50 : ")
print(square)
square.insert(4,25)
print("\n After inserting new element to fifth position : ")
print(square)
square.pop()
print("\n After removing last element : ")
print(square)
