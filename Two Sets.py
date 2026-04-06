def two_sets(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    if sum % 2 != 0:
        print("NO")
        return
    set1= set()
    set2 = set()
    part_sum = sum//2
    for i in range(n,0,-1):
        if  part_sum - i >= 0:
            set2.add(i)
            part_sum -= i
        else:
            set1.add(i)
    print("YES")
    print(len(set1))
    print(" ".join(map(str, set1)))  
    print(len(set2))
    print(" ".join(map(str, set2)))

two_sets(int(input()))