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

camp_activities = ["Cultural Immersion, (5 days, Easy, $800 fee)", "Kayaking and Pancakes, (3 days, Moderate, $400 fee)", "Mountain Biking, (4 days, Difficult, $900 fee)"]

print("These are the activities that our camp offers:")
print(F"1. {camp_activities[0]}")
print(F"2. {camp_activities[1]}")
print(F"3. {camp_activities[2]}")

while True:
    try:
        activity_chosen = int(input("Please enter either 1, 2 or 3 for your chosen activity: "))
        if activity_chosen in [1, 2, 3]:
            break
        else:
            print(f"Please enter either 1 for {camp_activities[0]}, 2 for {camp_activities[1]}, or 3 for {camp_activities[2]}.")
    except ValueError:
        print("Invalid input, please put a number.")

if activity_chosen == 1:
    activity_fee = 800
elif activity_chosen == 2:
    activity_fee = 400
elif activity_chosen == 3:
    activity_fee = 900

if activity_chosen == 1:
    name_of_activity = (f"{camp_activities[0]}")
elif activity_chosen == 2:
    name_of_activity = (f"{camp_activities[1]}")
elif activity_chosen == 3:
    name_of_activity = (f"{camp_activities[2]}")

meal_options = ["Standard", "Vegetarian", "Vegan"]

print("Please pick a meal option from our list:")

print(f"1. {meal_options[0]}")
print(f"2. {meal_options[1]}")
print(f"3. {meal_options[2]}")

while True:
    try:
        chosen_meal = int(input("Please enter the meal option youd like. Type either 1, 2, or 3: "))
        if chosen_meal in [1, 2, 3]:
            break
        else:
            print(f"Please enter either 1 for {meal_options[0]}, 2 for {meal_options[1]}, or 3 for {meal_options[2]}")
    except ValueError:
        print("Invalid input. Please enter a number.")


if chosen_meal == 1:
    meal_name = (f"{meal_options[0]}")
elif chosen_meal == 2:
    meal_name = (f"{meal_options[1]}")
elif chosen_meal == 3:
    meal_name = (f"{meal_options[2]}")


while True:
    shuttle_bus = input("Will you be needing a shuttle bus to get there? it will cost $80. Please enter Yes or No: ")
    shuttle_bus = shuttle_bus.lower()
    if shuttle_bus == "yes" or shuttle_bus == "no":
        break
    else:
        print("Please enter either Yes if youd like to get on the shuttle bus to get there for $80, or no if you will be driving there yourself.")

print("Picked yes for shuttle bus + $80")
print("Thank you")

if shuttle_bus == "yes":
    bus_fee = 80
elif shuttle_bus == "no":
    bus_fee = 0

print(f"Kiora {first_name}, please check these details are correct.")
while True:
    final_question = input(f"13 years old, picked activity - {name_of_activity}, picked meal option - {meal_name}, shuttle bus - {shuttle_bus}. Would you like to confirm this? Yes or No: ")
    final_question = final_question.lower()
    if final_question == "yes" or shuttle_bus == "no":
        break
    else:
        print("Please enter yes to confirm plan or no to cancel.")


