year_addition = 0

era = input("Please type S, H, or R: ")
if era == "S":
    year_addition = 1925
elif era == "H":
    year_addition = 1988
elif era == "R":
    year_addition = 2018

#Note: this simple script cannot handle errors such as input other than SHR. This issue is addressed in the next version of the script [see H0008]

japanese_year = input("Please input the Japanese year: ")

seireki_year = int(japanese_year) + year_addition
print("Your year is: " + str(seireki_year) + ".")
