def odd_range(start, stop, step):
    return (i for ind,i in enumerate(list(i for i in range(start, stop) if i%2 != 0)) if ind%step == 0 )

    
#print(list(odd_range(1, 10, 1)))  
#   returns a generator that produces [1, 3, 5, 7, 9]
print(list(odd_range(100, 150, 5)))
#   returns a generator that produces [101, 111, 121, 131, 141]
#print(list(odd_range(10, 0, 1))) 
#   returns a generator that produces []