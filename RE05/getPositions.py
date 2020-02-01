# getPositions.py
#def get_positions(word_list,sentence):
word_list = ["hello", "brave", "hello"]
sentence = "hello hello"
sentence_list = sentence.split()
position1 = '0'
position2 = ' 0'


if sentence_list[0] == sentence_list[1]:
    for i in range(3):
        if sentence_list[0] == word_list[i]:
            position1 = str(i)
            keeper = i
            break
    for i in range(keeper+1,3):
        if sentence_list[1] == word_list[i]:
            position2 = ' ' + str(i)
else:     
    if sentence_list[0] == word_list[0]:
        position1 = '0'
    elif sentence_list[0] == word_list[1]:
        position1 = '1'
    elif sentence_list[0] == word_list[2]:
        position1 = '2'
    if sentence_list[1] == word_list[0]:
        position2 = ' 0'
    if sentence_list[1] == word_list[1]:
        position2 = ' 1'
    if sentence_list[1] == word_list[2]:
        position2 = ' 2'

position = position1 + position2
print(position)



