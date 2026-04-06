def missingNumber(n, line):
    arr = list(map(int, line.split()))
    arr.sort()
    for i in range(1,n):
        if arr[i-1] != i:
            return i
    return n

print(missingNumber(int(input()), input()))   




