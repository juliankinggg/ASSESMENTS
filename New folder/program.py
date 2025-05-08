#asks user for first name
while True:
    first_name = input("Please enter your first name: ")
    if len(first_name) > 0:
        break
    else:
        print("Please enter a valid input")

min_age = 5
max_age = 17

#asks the user for their age 
while True:
    try:
        age = int(input(f"Kiora {first_name}, Please enter your age: "))
        if age >= min_age and age <= max_age :
            break
        else:
            print(f"You must be {min_age} - {max_age} Years old to attend")
    except ValueError:
        print("Please enter a valid input")

print("Thank You!")

#A list for the activities
camp_activities = ["Cultural Immersion, (5 days, Easy, $800 fee)", "Kayaking and Pancakes, (3 days, Moderate, $400 fee)", "Mountain Biking, (4 days, Difficult, $900 fee)"]

#Prints out the list of activities of the camp
print("These are the activities that our camp offers:")
print(F"1. {camp_activities[0]}")
print(F"2. {camp_activities[1]}")
print(F"3. {camp_activities[2]}")

#Asks the user which activity they want to partake in
while True:
    try:
        activity_chosen = int(input("Please enter either 1, 2 or 3 for your chosen activity: "))
        if activity_chosen in [1, 2, 3]:
            break
        else:
            print(f"Please enter either 1 for {camp_activities[0]}, 2 for {camp_activities[1]}, or 3 for {camp_activities[2]}.")
    except ValueError:
        print("Invalid input, please put a number.")

#sets the price value of the activities
if activity_chosen == 1:
    activity_fee = 800
elif activity_chosen == 2:
    activity_fee = 400
elif activity_chosen == 3:
    activity_fee = 900

#sets the name for the activities
if activity_chosen == 1:
    name_of_activity = (f"{camp_activities[0]}")
elif activity_chosen == 2:
    name_of_activity = (f"{camp_activities[1]}")
elif activity_chosen == 3:
    name_of_activity = (f"{camp_activities[2]}")

#A list for the meal options
meal_options = ["Standard", "Vegetarian", "Vegan"]

#prints the meal options the camp has
print("Please pick a meal option from our list:")

print(f"1. {meal_options[0]}")
print(f"2. {meal_options[1]}")
print(f"3. {meal_options[2]}")

#asks the user which meal option theyd like
while True:
    try:
        chosen_meal = int(input("Please enter the meal option youd like. Type either 1, 2, or 3: "))
        if chosen_meal in [1, 2, 3]:
            break
        else:
            print(f"Please enter either 1 for {meal_options[0]}, 2 for {meal_options[1]}, or 3 for {meal_options[2]}")
    except ValueError:
        print("Invalid input. Please enter a number.")

#gives the meals names
if chosen_meal == 1:
    meal_name = (f"{meal_options[0]}")
elif chosen_meal == 2:
    meal_name = (f"{meal_options[1]}")
elif chosen_meal == 3:
    meal_name = (f"{meal_options[2]}")

#asks the user if they need to go on the shuttle bus or not
while True:
    shuttle_bus = input("Will you be needing a shuttle bus to get there? it will cost $80. Please enter Yes or No: ")
    shuttle_bus = shuttle_bus.lower()
    if shuttle_bus == "yes" or shuttle_bus == "no":
        break
    else:
        print("Please enter either Yes if youd like to get on the shuttle bus to get there for $80, or no if you will be driving there yourself.")

#outcome of the question above
if shuttle_bus == "yes":
    print("Picked yes for shuttle bus + $80")
    print("Thank you!")
elif shuttle_bus == "no":
    print("no shuttle bus!")
    print("This means you will have to drive there yourself!")

#Sets the price for the shuttle bus
if shuttle_bus == "yes":
    bus_fee = 80
elif shuttle_bus == "no":
    bus_fee = 0

#Final question that infroms the user of their detail and asks if they would like to confirm it.
print(f"Kiora {first_name}, please check if these details are correct:")
print(f"{age} years old.")
print(f"Picked avtivity - {name_of_activity}")
print(f"Picked meal option - {meal_name}")
print(f"Shuttle bus - {shuttle_bus}")
print(f"The total cost will be ${bus_fee + activity_fee}.")
while True:
    final_question = input("Would you like to confirm this booking? y/yes or n/no: ")
    final_question = final_question.lower()
    if final_question == "yes" or final_question == "no" or final_question == "y" or final_question == "n":
        break
    else:
        print("Please enter y/yes to confirm plan or n/no to cancel.")

#final question outcome
if final_question == "yes" or final_question == "y":
    print("Booking confirmed. Thank you for choosing our camp. Enjoy!")
elif final_question == "no" or final_question == "n":
    print("Booking cancelled!")