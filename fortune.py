# Describe the program to the user
print ("Welcome!")
print("")
print ("\t This program is designed as a game that will tell you your fortune!")
print("")

# Prompt user for input data
user_name = input ("Please enter your name: ")
user_age_str = input ("Please enter your age: ")
fav_color = input ("Please enter your favorite color: ")
fav_number_str = input ("Please enter your favorite number: ")

# Convert possible strings to integers
user_age = int (user_age_str)
fav_number = int (fav_number_str)

print ("")

# Assign variable names for fortunes
fortune1 = ("Today it's up to you to create the peacefulness you long for.")
fortune2 = ("A friend asks only for your time not your money.")
fortune3 =  ("If you refuse to accept anything but the best, you very often get it.")
fortune4 =  ("Enjoy the good luck a companion brings you.")
fortune5 = ("A smile is your passport into the hearts of others.")
fortune6 =  ("A good way to keep healthy is to eat more Chinese food.")
fortune7 =  ("Your high-minded principles spell success.")
fortune8 =  ("Hard work pays off in the future, laziness pays off now.")
fortune9 =  ("Change can hurt, but it leads a path to something better.")


# The first chucnk has four conditions. I have chunked them according to age.
# If the user is younger than 18 years old the program must go through each of these
#  if/elif/else condtions before receiving their fortune.
if user_age < 18 :
    if fav_color == "green" :
        print ( user_name , ", you have received Fortune 1: " + fortune1 )
    elif fav_color == "blue" :
        print (user_name , ", you have received Fortune 2: " , fortune2 )

    else :
        if fav_number < 50 :
            print (user_name , ", you have received Fortune 3: " , fortune3 )
        elif fav_number >= 50 :
            print (user_name , ", you have received Fortune 4: " , fortune4 )

# The second chunk of filters/conditions pertain to user's who are older than 18.
# The program must go through a series of if/elif/else statements before receiving their fortune.
if user_age > 18 :
    if fav_color == "orange" :
        if fav_number <= 5 :
            print (user_name , ", you have received Fortune 5: " , fortune5 )
        elif fav_number > 5 :
            print (user_name , ", you have received Fortune 6: " , fortune6 )
    else:
        print (user_name , ", you have received Fortune 7:" , fortune7 )


# The third chunk of filters/conditions pertain to user's who are exactly 18.
# The program must go through a series of if/elif/else statements before receiving their fortune.
if user_age == 18 :
    if fav_number != 3 :
        print (user_name , ", you have received Fortune 8: " , fortune8 )
    else:
        print (user_name , ", you have received Fortune 9: " , fortune9)

print ("")
print ("Is it fate?")
print("")
print ("\t Is is destiny?")
print("")
print ("\t\t You decide!")
