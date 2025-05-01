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
            print("Please enter either 1, 2 or 3 and pick an activity.")
    except ValueError:
        print("Invalid input, please put a number.")

        