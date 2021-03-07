# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

#Run Conditionals
if(user_choice == "r" and computer_choice == "p"):
    print("You chose rock. The computer chose paper.")
    print("Sorry, You lose.")

elif(user_choice == "r" and computer_choice == "s"):
    print("You chose rock. The computer chose scissors.")
    print("You won!")

if(user_choice == "r" and computer_choice == "r"):
    print("You chose rock. The computer chose rock.")
    print("A smashing tie!")

elif(user_choice == "r" and computer_choice == "s"):
    print("You chose rock. The computer chose scissors.")
    print("You won!")

# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    user_number = input("How many numbers?")
    # Loop through the numbers. (Be sure to cast the string into an integer.)
   for x in range(start_number, int(user_number)+start_number):

        # Print each number in the range
       print(x)
    
    # Set the next start number as the last number of the loop
    start_number = start_number + int(user_number)
    
    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")


    # Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(f'{row[0]} + " is rated " + row[1] + " with a rating of " + row[5])
    else:
        print("Sorry about this, we don't seem to have what you are looking for!")

        # Dependencies
import os

# Specify the file to write to
file_outpath = os.path.join("..", "output", "Employee_Data.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file_outpath, 'w') as textfile:

    # Create a variable to hold text inside parentheses.
    employee_data = (
        f"\nLast Name\tFirst Name\tEID\n"
        f"-------------------------------------\n"
        f"Frost\t\tCaleb\t\tCF505\n"
        )

    # Write the text to the file.
    textfile.write(employee_data)
    # Print the data to the screen.
    print(employee_data)

    # Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")

# Specify the file to write to the movie data.
txtpath = os.path.join("..", "output", "netflix_data.txt")

# Set a variable to false to check if we found the video
found = False

# Open the NetFlix CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:

            # Set the variable created to confirm we have found the video
            found = True

            # Open the file using "write" mode. Specify the variable to hold the contents
            with open(txtpath, 'w') as textfile:
                
                # Create a variable to hold the title, rating level, and the movie rating inside parentheses.
                netflix_data = (
                    f"Title: {row[0]}\n"
                    f"Rating Level: {row[1]}\n"
                    f"Rated: {row[5]}\n"
                    )
                
                # Write the movie data to the text file.
                textfile.write(netflix_data)

                # Print the movie data to the console.
                print(netflix_data)

            # Stop at first results to avoid duplicates
            break

    # If the video is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")