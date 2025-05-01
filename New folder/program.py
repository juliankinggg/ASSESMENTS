#asks user for first name
while True:
    first_name = input("Please enter your first name: ")
    if len(first_name) > 0:
        break
    else:
        print("Please enter a valid input")

#asks the user for their age 
while True:
    try:
        age = int(input("Please enter your age: "))
        if age > 4 and age < 18 :
            break
        else:
            print("You must be 5 - 17 Years old to attend")
    except ValueError:
        print("Please enter a valid input")


