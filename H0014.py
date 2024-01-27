import unicodedata

def normalization_NFKC(x):
    if unicodedata.is_normalized("NFKC", x):
        yn_flag = True
        char_list = "None found"
        normalized_term = "Same as original"
    else:
        yn_flag = False
        char_list = "|"
        for letter in x:
            if not unicodedata.is_normalized("NFKC", letter):
                char_list = char_list + letter + "|"
        normalized_term = unicodedata.normalize("NFKC", x)

    return [yn_flag, char_list, normalized_term]



my_writefilepath = r"C:\Users\benj\Documents\Test Folder\converted_termlist.txt"

orig_termlist = ["ｐｙｔｈｏｎ", "born in １９８５", "℃"]

my_writefilepath = open(my_writefilepath, "a")

for term in orig_termlist:
    output_list = normalization_NFKC(term)


    my_writefilepath.write("Original term:" + term + "\n"
                           "Non-normalized characters found: " + output_list[1] + "\n" +
                           "Normalized term:" + output_list[2] + "\n\n")


my_writefilepath.close()
