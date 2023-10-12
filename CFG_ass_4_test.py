print("The story starts like this, as all good stories should... 'Once upon a time...'")
line_1 = "Once upon a time, "
# line_2 = input("What do you think the next line should be? ")
# print(line_1 + line_2)

# Display options to the user
print("Now you need to choose how this sentence finishes:")
print("    1. Donna really struggled to use GitHub. ")
print("    2. Donna was absolutely loving using GitHub. ")
print("    3. Donna shut her computer and went to bed. She will try again tomorrow. ")

# Get user input
choice = input("Enter the number to continue the story: (1, 2 or 3): ")

# Convert the input to an integer
choice = int(choice)

# Process the user's choice
if choice == 1:
    print(line_1 + "Donna really struggled to use GitHub. ")
elif choice == 2:
    print(line_1 + "Donna was absolutely loving using GitHub. ")
elif choice == 3:
    print(line_1 + "Donna shut her computer and went to bed. She will try again tomorrow. ")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")


