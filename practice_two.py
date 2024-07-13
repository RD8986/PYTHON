# PRACTICE 2
# 1. Create a list of the first 20 natural numbers.
# 2. Slice the list to get the first 10 elements.
# 3. Slice the list to get the last 5 elements.
# 4. Print both slices.

Natural_Numbers=list(range(1,21))
print(Natural_Numbers)
first10=Natural_Numbers[:10]
last5=Natural_Numbers[-5:]
print("\n First 10 elements : ")
print(first10)
print("\n Last 5 elements : ")
print(last5)