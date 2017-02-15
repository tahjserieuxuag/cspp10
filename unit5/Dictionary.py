import pprint
dictionary = {}
def add(dictionary):
    
    task = input("What would you like to do: ") 
    if task == "add":
        add_key = input("What key do you want to add: ")
        add_value = input("What value would you like to add: ")
        dictionary[add_key] = add_value
        print(dictionary)
add()