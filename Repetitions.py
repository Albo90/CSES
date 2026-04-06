def repetitions(string):
    previous_char = ""
    count = 0 
    res = 0
    for char in string:
        if char == previous_char:
            count+=1
        else:
            count = 1
            previous_char = char    
        if count > res :
            res = count
    return res

print(repetitions(input()))
