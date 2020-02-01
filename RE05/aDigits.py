# aDigits


def adigits(str1, str2, str3):
    result = ''
    listint = [int(str1), int(str2), int(str3)]
    if (listint[0] >= listint[1]) and (listint[0] >= listint[2]):
        if (listint[2] >= listint[1]):
            temp = listint[1]
            listint[1] = listint[2]
            listint[2] = temp
    if (listint[1] >= listint[0]) and (listint[1] >= listint[2]):
        temp = listint[0]
        listint[0] = listint[1]
        listint[1] = temp
        if (listint[2] >= listint[1]):
            temp = listint[1]
            listint[1] = listint[2]
            listint[2] = temp
    if (listint[2] >= listint[0]) and (listint[2] >= listint[1]):
        temp = listint[0]
        listint[0] = listint[2]
        listint[2] = temp
        if (listint[2] >= listint[1]):
            temp = listint[1]
            listint[1] = listint[2]
            listint[2] = temp
    for x in listint:
        result += str(x)
    result = int(result)
    if result == 0:
        result = format(result, '03')
    return result


print(adigits(5, 5, 3))
