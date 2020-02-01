#manipulator.py
"""
1. insert i e: Insert integer e at position i.
2. print: Save list to result string.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list in ascending order.
6. pop: Remove the last element from the list.
7. reverse: Reverse the list.
"""

def manipulator(l, cmds):
    result = ""
    for cmd in cmds:
        cmdselect = cmd.split(' ', 1)[0] 
        
        if cmdselect == "insert":
            integer = int(cmd.split(' ')[2])
            position = int(cmd.split(' ')[1])
            l.insert(position, integer)
        elif cmdselect == "print":
            result += str(l) + " "
        elif cmdselect == "remove":
            integer = cmd.split(" ")[1]
            pos=-1
            for element in l:
                element = str(element)
                pos+=1
                if element == integer:
                    l = l[:pos] + l[pos+1:]
                    break
        elif cmdselect == "append":
            integer = int(cmd.split(" ")[1])
            l.append(integer)
        elif cmdselect == "sort":
            l.sort()
        elif cmdselect == "pop":
            l.pop()
        elif cmdselect == "reverse":
            l = l[::-1]
    return result
        
    
    
    

print(manipulator([], ["insert 0 5", "insert 1 10", "insert 0 6",
"print", "remove 6", "append 9", "append 1", "sort", "print",
"pop", "reverse", "print"]))