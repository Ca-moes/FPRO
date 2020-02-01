def exception_str(f):
    try:
        f()
    except Exception as ex:
#        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#        message = template.format(type(ex).__name__, ex.args)
#        print(ex)
        return ex
    else:
        return "No exception was raised"
        
  
print(exception_str(lambda: 1/0))
# returns the string "division by zero"
print(exception_str(lambda: 0))
# returns the string "no exception was raised"
