def permutations(n):
    if n > 1 and n <= 3:
        return "NO SOLUTION"
    eves = []
    odds = []
    for i in range(1,n+1):
        if i % 2 == 0:
            eves.append(i)
        else:
            odds.append(i)
    res = eves + odds
    return " ".join(map(str, res))

print(permutations(int(input())))