def weirdAlgorithm(n, line):
    line +=f" {n}" 
    if n == 1:
       return  line.strip()
    if n % 2 == 0:
        n = n // 2
        return weirdAlgorithm(n, line)
    else:
        n = 3 * n + 1
    return weirdAlgorithm(n, line)

print(weirdAlgorithm(int(input()), ""))