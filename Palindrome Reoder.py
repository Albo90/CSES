from collections import Counter
def palindrome_reoder(s):
    letters = Counter(s)
    is_odd_found = False
    res = ""
    center = ""
    for letter, count in reversed(letters.most_common()):
        if count%2 != 0:
            if is_odd_found:
                return "NO SOLUTION"
            is_odd_found = True
            center = letter
            count = count - 1
        res = letter*(count//2) + res + letter*(count//2)
    res = res[:len(res)//2] + center + res[len(res)//2:]    
    return res

print(palindrome_reoder(input()))



