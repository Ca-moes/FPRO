def greatest(num):
    num = str(num)
    num = sorted(num)
    num = num[::-1]
    result = ""
    for number in num:
        result+=number
    result = int(result)
    return result
    
    
