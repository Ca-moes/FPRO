#  (number of lines, number of words and number of characters)
def wc(filename):
    linecounter = 0
    wordcounter = 0
    charcounter = 0
    with open(filename, "r") as myfile:
        for the_line in myfile:
            linecounter += 1
            wordcounter += len(the_line.split())
            charcounter += len(list(the_line))
#            for i in list(the_line):
#                charcounter += 1
#                if i.isalpha():
#                    charcounter += 1
#            print(the_line, end="")
    return (linecounter, wordcounter, charcounter)

print(wc("shakespeare.txt"))
#  returns the tuple (14, 105, 611)
print()
print(wc("monty.txt"))
# returns the tuple (15, 155, 856)