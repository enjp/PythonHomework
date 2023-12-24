#Note: You can break up lists into multiple lines to make them more human-readable.
# I decided to do that here, but if the list was very long,
# it would probably be better to write it in a single line.

keyword_list = [
    "deg",
    "alpha",
    "section"
]

output_list = [
    "°",
    "α",
    "§"
]

#while loop to get and verify user input, or allow user to quit
while True:
    input_keyword = input("Please input keyword: ")
    if input_keyword == "quit":
        print("OK. Quitting now.")
        exit()
    elif input_keyword not in keyword_list:
        print("Keyword not found. Please try again, or type \"quit\" to exit.")
    else:
        break

obtained_index = keyword_list.index(input_keyword)

print("The corresponding item in the other list is:\n" + output_list[obtained_index])
