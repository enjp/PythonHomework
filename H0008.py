year_addition = 0

while True:
    era = input("Please type S, H, or R: ")
    if era != "S" and era != "H" and era != "R":
    #an alternative condition is as follows
    #if era not in "SHR":
        print("Input not recognized. Please try again.")
        #continue
        #↑最初はここでcontinueを入れていましたが、不要なことに気づきました。（ここの場合、あってもなくても全く同じ動作になります。）
    else:
        #when the above statement is NOT satisfied, the user input is correct, so we can break the loop
        break

if era == "S":
    year_addition = 1925
elif era == "H":
    year_addition = 1988
elif era == "R":
    year_addition = 2018

while True:
    japanese_year = input("Please input the Japanese year: ")
    if japanese_year.isdigit() == False:
        print("Please input numbers only")
    else:
        break


seireki_year = int(japanese_year) + year_addition
print("Your year is: " + str(seireki_year) + ".")
