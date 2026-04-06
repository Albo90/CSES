def two_knights(n):
    for i in range(1, n+1):
        print(_check_board(i))

def _check_board(k):
    res = (k**2)*(k**2-1)//2-4*(k-1)*(k-2)
    return int(res)

n = int(input())
two_knights(n)