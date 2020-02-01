import functools
def reduce_map_filter(args):
    if type(args[2]) is list:
        if args[0] == "map":
            return list(map(args[1], args[2]))
        if args[0] == "reduce":
            return functools.reduce(args[1], args[2])
        if args[0] == "filter":
            return list(filter(args[1], args[2]))
    else:
        a = (reduce_map_filter(args[2]),)
        args = args[:-1] + a
        return reduce_map_filter(args)

    
    
    
    
    
    
#print(reduce_map_filter(("map", lambda x: 2*x, [1,2,3]))) 
#  returns the list [2, 4, 6]


#print(reduce_map_filter(("map", lambda x: 2*x,("filter", lambda x: x%2 != 0,[1,2,3])))  )
#  returns the list [2, 6]


    print(reduce_map_filter(
            ("reduce", lambda a,b: a+b,
             ("map", lambda x: 2*x,
              ("filter", lambda x: x%2 != 0,
               [1,2,3])))) )

# returns the integer 8