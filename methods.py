import math

def floor(x):
    return math.floor(x)

def nroot(n, x):
    if x == 0:
        return 0  # 0のn乗根は0
    if n == 0:
        return 1  # 0乗根は1を返す
    if x < 0 and n % 2 == 0:
        return None  # 負の数の偶数根は実数解を持たない
    if x < 0 and n % 2 != 0:
        return int(-(abs(x) ** (1/n)))  # 負の数の奇数根を計算
    return int(x ** (1/n))  # 通常の根を計算

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
        # 97 - 97 = 0 ('a' - 'a' = 0) 
        cache[ord(str1[i]) - ord('a')] += 1
        cache[ord(str2[i]) - ord('a')] -= 1

    return max(cache) == 0 and min(cache) == 0



