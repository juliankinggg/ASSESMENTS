#asks user for first name
while True:
    first_name = input("Please enter your first name: ")
    if len(first_name) > 0 and not first_name.isdigit():
        break
    else:
        print("Please enter a valid input")
#Constants
min_age = 5
max_age = 17
leadership_age = 15
shuttle_bus_cost = 80

#asks the user for their age 
while True:
    try:
        camper_age = int(input(f"Kiora {first_name}, Please enter your age: "))
        if camper_age >= leadership_age and camper_age <= 17:
            leadership_offer = input("We offer a leadership role to those 15 years old or over. Would you like to be a candidate to be a camp leader? Please enter y/yer or n/no: ")
            leadership_offer = leadership_offer.lower()
            if leadership_offer == "yes" or leadership_offer == "y" or leadership_offer == "no" or leadership_offer == "n":
                break
            else:
                print("Invalid input. You must enter either y/yes or n/no")
        elif camper_age >= min_age and camper_age <= 14 :
            leadership_offer = "no"
            break
        else:
            print(f"You must be {min_age} - {max_age} Years old to attend")
    except ValueError:
        print("Please enter a valid input")  

if leadership_offer == "yes" or leadership_offer == "y":
    leadership_answer = "YES"
elif leadership_offer == "no" or leadership_offer == "n":
    leadership_answer = "NO"

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
    shuttle_bus = input(f"Will you be needing a shuttle bus to get there? it will cost ${shuttle_bus_cost}. Please enter y/yes or n/no: ")
    shuttle_bus = shuttle_bus.lower()
    if shuttle_bus == "yes" or shuttle_bus == "no" or shuttle_bus == "y" or shuttle_bus == "n":
        break
    else:
        print(f"Please enter either Yes if youd like to get on the shuttle bus to get there for ${shuttle_bus_cost}, or no if you will be driving there yourself.")

#outcome of the question above
if shuttle_bus == "yes" or shuttle_bus == "y":
    print(f"Picked yes for shuttle bus + ${shuttle_bus_cost}")
    print("Thank you!")
elif shuttle_bus == "no" or shuttle_bus == "n":
    print("no shuttle bus!")
    print("This means you will have to drive there yourself!")

#Sets the price for the shuttle bus
if shuttle_bus == "yes" or shuttle_bus == "y":
    bus_fee = shuttle_bus_cost
    bus_answer = "yes"
elif shuttle_bus == "no" or shuttle_bus == "n":
    bus_fee = 0
    bus_answer = "no"

#Final question that infroms the user of their detail and asks if they would like to confirm it.
camper_details = [f"{camper_age} years old.", f"Picked activitiy - {name_of_activity}.", f"Picked meal option - {meal_name}.", f"Going to shuttle bus? - {bus_answer}.", f"The total cost will be ${bus_fee + activity_fee}.", f"Camp leadership - {leadership_answer}."]
print(f"Kiora {first_name}, please check if these details are correct: {camper_details[0]} {camper_details[1]} {camper_details[2]} {camper_details[3]} {camper_details[4]} {camper_details[5]}")


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