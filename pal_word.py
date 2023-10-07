def is_palindrome(input_string):
    # Remove spaces from the input string and convert it to lowercase
    cleaned_string = input_string.replace(" ", "").lower()
    # Compare the cleaned string with its reverse
    return cleaned_string == cleaned_string[::-1]
print(is_palindrome("Never Odd or Even"))  # Should be True
print(is_palindrome("abc"))  # Should be False
print(is_palindrome("kayak"))  # Should be True
