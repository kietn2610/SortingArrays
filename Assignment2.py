# Array of numbers and people
numbers = [645.41, 37.59, 76.41, 5.31, -34.23, 1.11, 1.10, 23.46, 635.47, -876.32, 467.83, 62.25]
people={'Hal' : 20 , 'Susann': 31 , 'Dwight' : 19 , 'Kassandra': 21 ,'Lawrence' : 25 , 'Cindy': 22 ,
         'Cory' : 27 , 'Mac': 19 ,'Romana' : 27 , 'Doretha': 32 ,'Danna' : 20 , 'Zara': 23 ,
         'Rosalyn' : 26, 'Risa': 24 , 'Benny' : 28 , 'Juan': 33 ,'Natalie' : 25}

# Duct Typing
class Nums:
    def sortNums(self):
        res = sorted(numbers, key=lambda x: float(x))
        print('Sorted Numbers: ', str(res))


class Dict:
    def sortDict(self):
        abc_sorted = dict(sorted(people.items()))
        num_sorted = dict(sorted(people.items(), key=lambda item: item[1]))
        print('Sorted People in Alphabetical Order: ', abc_sorted)
        print('Sorted People in Numerical Order: ', num_sorted)


class Printout:
    def printNums(self, nums):
        nums.sortNums()

    def printDict(self, list2):
        list2.sortDict()

# Calling the printout class
display = Printout()

# Calling nums class and printNums in display class
list1 = Nums()
display.printNums(list1)

# Calling dict class and printDict in display class
list2 = Dict()
display.printDict(list2)
