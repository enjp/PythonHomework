#Method 1
user_input = input("Input the year in Showa: ")

western_year = 1925 + int(user_input)

print("The western year is: " + str(western_year))

#Method 2 - The last two steps from method 1 are combined

#Instead of using the variable "western year", I simply wrote the entire content of "western_year" in the final print command

user_input = input("Input the year in Showa: ")

print("The western year is: " + str(1925 + int(user_input)))

#Method 3 - Finally, in a manner similar to the above, the two lines of method 2 are merged into one line. Very hard to read, so I don't recommend it!

print("The western year is: " + str(1925 + int(input("Input the year in Showa: "))))
