def countVowelStrings(n: int) -> int:
    dp = [[0] * 5 for _ in range(n)]
    
    # Initialize base cases
    for i in range(5):
        dp[0][i] = 1
    
    # Populate the dp array
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = sum(dp[i-1][j:])
    
    return sum(dp[n-1])

# Test Cases
print(countVowelStrings(1))  # Output: 5
print(countVowelStrings(2))  # Output: 15
