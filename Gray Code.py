def gray_code(n):
    for i in range(1 << n):
        yield(f"{i ^ (i >> 1):0{n}b}")


print(*list(gray_code(int(input()))))