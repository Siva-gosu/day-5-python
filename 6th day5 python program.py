def delchar(s, c):
    # Check if c has length 1
    if len(c) != 1:
        return s
    
    # Remove all occurrences of c from s
    new_s = s.replace(c, "")
    
    return new_s

# Test the function
input_string = input("Enter the string: ")
character_to_delete = input("Enter a character to be deleted: ")
output_string = delchar(input_string, character_to_delete)
print("String after the character is removed:", output_string)
