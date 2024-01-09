#Change the following filepaths as necessary

my_readfilepath = r"C:\Users\benj\Documents\Test Folder\test.txt"
my_writefilepath = r"C:\Users\benj\Documents\Test Folder\outputlastline.txt"

my_readfile = open(my_readfilepath, "r")

my_readlines = my_readfile.readlines()

my_readfile.close()

my_writefilepath = open(my_writefilepath, "a")

my_writefilepath.write(my_readlines[-1])

my_writefilepath.close()
