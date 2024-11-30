import math

def floor(x):
    return math.floor(x)

def nroot(n, x):
    if x == 0:
        return 0
    if n == 0:
        return 1
    if x < 0 and n % 2 == 0:
        return None
    if x < 0 and n % 2 != 0:
        return int(-(abs(x) ** (1/n)))
    return int(x ** (1/n))

def reverse(s):
    return s[::-1]

def isAnagram(s1, s2):
    str1 = s1.lower().replace(' ', '')
    str2 = s2.lower().replace(' ', '')

    if len(str1) != len(str2):
        return False
    
    cache = []
    for i in range(26):
        cache.append(0)

    for i in range(len(str1)):
        cache[ord(str1[i]) - ord('a')] += 1
        cache[ord(str2[i]) - ord('a')] -= 1

    return max(cache) == 0 and min(cache) == 0



