def coin_piles(a, b):
    if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b):
        return "YES"
    return "NO"

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(coin_piles(a,b))