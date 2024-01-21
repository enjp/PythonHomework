import unicodedata

my_writefilepath = r"C:\Users\benj\Documents\Test Folder\converted_termlist.txt"

orig_termlist = ["ｐｙｔｈｏｎ", "born in １９８５", "℃"]

my_writefilepath = open(my_writefilepath, "a")

for term in orig_termlist:
    my_writefilepath.write(unicodedata.normalize("NFKC", term) + "\n")

my_writefilepath.close()
