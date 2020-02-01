#roman_to_integer.py
"""
If the value of the current roman symbol is greater than or equal to the value of the next
symbol, then add this value to the running total; otherwise subtract this value to the running
total.
"""
mapping = {"I":1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
def roman_to_integer(astring):
    result = 0
    for index,symbol in enumerate(astring):
        if index <= len(astring)-2:
            if mapping[astring[index]] >= mapping[astring[index+1]]:
                result += mapping[astring[index]]
            else:
                result -= mapping[astring[index]]
        else:
            result += mapping[astring[index]]
    return result
    
    
print(roman_to_integer('LXXXIV'))
