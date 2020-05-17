def scarletgrocerylist(): #Omar: header that includes the keyword "def", which indicates that this is a function definition, below is the body#

    n1 = int(input("Enter number of food categories : ")) #Omar: variable n1 represents the number of food categories; it is equal to an integer value that the user inputs via the input function#

    for i in range(0, n1): #Omar: for loop that loops as long as the inputted number of food categories is >= 0 and <= the value for n1#

        food_category = input("Enter a food category : ") #Omar: the variable "food_category" is equal to the user's input (a prompt is also included)#

        n2 = int(input("Enter number of food items : ")) #Omar: variable n2 represents the number of food items for each food category; it is equal to an  integer value that the user inputs via the input function#

        food_item = [] #Omar: the variable "food_item" is equal to an empty list, this allows the list to have elements added to it#

        for i in range(0, n2): #Lindsey: for loop that loops as long as the inputted number of items is >= 0 and <= the value for n2#

            item = input("Enter a food item : ") #Lindsey: the variable "item" is equal to the user's input (a prompt is also included)#

            food_item.append(item) #Lindsey: this allows a food item to be added to the list named "food_item" via the append method#

        food_item.sort() #Lindsey: the list method "sort" is utilized to alphabetically sort each item in a given list# 

        foodcategory_fooditem = {} #Adil: the variable "foodcategory_fooditem" is equal to an empty dictionary, this allows the dictionary to take in a key-value pair#

        foodcategory_fooditem[food_category] = food_item #Adil: this assigns the value named "food_item" to the key named "food_category"#

        print(foodcategory_fooditem) #Esha: this output prints the completed dictionary regarding each food category and its respective item(s)#

        print("The number of food items is", len(food_item)) #Esha: this output prints a string and the length of the list named "food_item", which        indicates how many food items are assigned to a particular food category; also, the length function demonstrates polymorphism due to its applicability to other    types, such as strings, arrays, and tuples#

