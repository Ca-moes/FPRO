#find_dtype.py
def  find_dtype(atuple, data_type):
    restuple = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            restuple += (i,)
    return restuple
    

