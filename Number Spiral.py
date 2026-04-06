def numberSpiral(line):
    arr = list(map(int, line.split()))
    x, y = arr[0], arr[1]
    if x == y:
        return (x)*(x)-(x-1)
    diag = max(x,y) 
    diag_value = (diag)*(diag)-(diag-1)
    if x > y:
        if x%2 != 0:
            return diag_value - (diag - y)
        else:            
            return diag_value + (diag - y)
    else:       
        if y%2 != 0:
            return diag_value + (diag - x)
        else:            
            return diag_value - (diag - x)      

n = int(input())
for i in range(n):
    print(numberSpiral(input()))          
