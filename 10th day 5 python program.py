def isScramble(s1: str, s2: str) -> bool:
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False
    
    n = len(s1)
    memo = {}

    def dfs(i1, i2, length):
        if (i1, i2, length) in memo:
            return memo[(i1, i2, length)]

        if s1[i1:i1 + length] == s2[i2:i2 + length]:
            memo[(i1, i2, length)] = True
            return True

        if sorted(s1[i1:i1 + length]) != sorted(s2[i2:i2 + length]):
            memo[(i1, i2, length)] = False
            return False

        for i in range(1, length):
            if (dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i)) or \
               (dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i)):
                memo[(i1, i2, length)] = True
                return True

        memo[(i1, i2, length)] = False
        return False

    return dfs(0, 0, n)

# Example usage:
s1 = "great"
s2 = "rgeat"
print(isScramble(s1, s2))  # Output: True
