def isPalindrome(s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the clean string is equal to its reverse
    return clean_s == clean_s[::-1]

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
