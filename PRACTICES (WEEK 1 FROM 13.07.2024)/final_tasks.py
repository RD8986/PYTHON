# FINAL TASK (ALL 12 TASK COMBINED)

def task1():
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

def task2():
    Natural_Numbers=list(range(1,21))
    print(Natural_Numbers)
    first10=Natural_Numbers[:10]
    last5=Natural_Numbers[-5:]
    print("\n First 10 elements : ")
    print(first10)
    print("\n Last 5 elements : ")
    print(last5)
    
def task3():
    oddnumbers=[i for i in range(1,20,2)]
    print(oddnumbers)
    squareodd=[i**2 for i in oddnumbers]
    print(squareodd)
    
def task4():
    fivecontinents = ("Africa", "Asia", "Europe", "North America", "South America")
    print(fivecontinents[2]) 
    try:
        fivecontinents[1] = "Australia"
    except TypeError as a:
        print(f"Error occurred: {a}")
        
def task5():
    mytuple=(1,"Amit",1.25)
    a,b,c=mytuple
    print("\n First variable : ")
    print(a)
    print("\n Second variable : ")
    print(b)
    print("\n Third variable : ")
    print(c)
    
def task6():
    mytuple=((1, 2, 3), (4, 5, 6))
    secon_element_of_first_tupple=mytuple[0][1]
    first_element_of_secondtupple=mytuple[1][0]
    print("\n Second element of first tupple : ")
    print(secon_element_of_first_tupple)
    print("\n First element of second tupple : ")
    print(first_element_of_secondtupple)
    
def task7():
    first_five_oddnumbers={1, 3, 5, 7, 9}
    first_five_evennumbers={2, 4, 6, 8, 10}

    union=first_five_oddnumbers.union(first_five_evennumbers)
    intersection=first_five_oddnumbers.intersection(first_five_evennumbers)
    print("\n Union of first five odd & even numbers : ")
    print(union)
    print("\n Intersection of first five odd & even numbers : ")
    print(intersection)
    
def task8():
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
    
def task9():
    vowels = {"a", "e", "i", "o", "u"}
    print(vowels)

    if "e" in vowels:
        print(" E is in the set of vowels.")
    else:
        print("E is not in the set of vowels.")

    if "x" in vowels:
        print("X is in the set of vowels.")
    else:
        print("X is not in the set of vowels.")
        
def task10():
    student = {"name": ["Anand", "Amit", "Roshani"], "age": [21, 18, 17], "grades": [85, 92, 78]}
    print(student)

    student["age"] = 19, 24, 19
    print("\n After updating age of student's : ")
    print(student)
    student["Subjects"] = ["Math", "Science", "English"]
    print("\n After adding Subjects key and value : ")
    print(student)
    
def task11():
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
    
def task12():
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
    
while True:
    try:
        x = int(input("\nPlease enter a task number (1-12) or 0 to exit: "))
        if x < 0 or x > 12:
            print("Please enter a number between 1 and 12 or 0 to exit.")
        elif x == 0:
            print("Thank you! Exiting successfully.")
            break
        else:
            if x == 1:
                task1()
            elif x == 2:
                task2()
            elif x == 3:
                task3()
            elif x == 4:
                task4()
            elif x == 5:
                task5()
            elif x == 6:
                task6()
            elif x == 7:
                task7()
            elif x == 8:
                task8()
            elif x == 9:
                task9()
            elif x == 10:
                task10()
            elif x == 11:
                task11()
            elif x == 12:
                task12()
    except ValueError as e:
        print(f"{e}. Please enter a number.")