# Shamir Roy

# Task - 1
def isPalindrome(S,newS, index):

    newS += S[index]
    if index == 0:
        return S == newS
    else:
        return  isPalindrome(S, newS, index - 1)

S = 'a'
print(isPalindrome(S,'',len(S) - 1))
# Time Complexity - O(n)
# Space Complexity - O(1)



# Task - 2

def multiply(a, b, index, sum):

    sum += a
    if index + 1 == abs(b):
        if b < 0 :
            return -sum
        else:
            return sum
    else:
        return multiply(a, b, index + 1, sum)

# Checking all possible distinct test cases
print(multiply(-5,-6,0,0))
print(multiply(5,-6,0,0))
print(multiply(6,7,0,0))
print(multiply(-6,7,0,0))


# Time Complexity - O(n)
# Space Complexity - O(1)