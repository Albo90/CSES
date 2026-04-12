permutations = set()
def create_string(index, s_list):
    if index == len(s_list):
        permutations.add(''.join(s_list))
    chars = set()    
    for i in range(index, len(s_list)):
        if s_list[i] in chars:
            continue
        chars.add(s_list[i])
        s_list[index], s_list[i] = s_list[i], s_list[index]
        create_string(index + 1, s_list)
        s_list[index], s_list[i] = s_list[i], s_list[index]
    return sorted(permutations)

s = input()
s = create_string(0, list(s))
print(len(s))
print(*s, sep='\n')