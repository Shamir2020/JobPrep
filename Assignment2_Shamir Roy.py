# Shamir Roy

# Task 1
s = 'dosta'
indices = [4,0,1,2,3]


def SearchVal(array, element):

    for i in range(len(array)):
        if array[i] == element:
            return i

    return -1

s2 = ''
for i in range(len(indices)):
    s2 += s[SearchVal(indices, i)]

print(s2)

# Time Complexity - O(n*n)
# Space Complexity - O(1)



# Tasl 2

def SearchStr(haystack, needle):

    c = 0
    val = ''
    d = 0
    for i in range(len(haystack)):
        if haystack[i] == needle[d]:
            if val == '':
                c = i
            val += haystack[i]
        d += 1

        if val == needle:
            return c

        if d >= len(needle):
            d = 0
            val = ''

    return  -1


print(SearchStr('codemama', 'ostad'))

# Time Complexity - O(n)
# Space Complexity - O(1)