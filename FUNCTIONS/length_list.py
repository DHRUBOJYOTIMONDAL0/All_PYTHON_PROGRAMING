cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
heroes = ["Superman", "Batman", "Wonder Woman", "Spiderman", "Iron Man", "Thor", "Hulk"]
# print(len(cities))

def length(list):
    print(len(list))
# length(cities)
# length(heroes) 


# elements of a list in a single line. 

def print_list(list):
    for element in list:
        print(element, end=" ")
print_list(heroes)
print()      