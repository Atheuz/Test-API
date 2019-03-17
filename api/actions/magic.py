"""Calculate some magic."""
import re


def calculate_longest_palindrome(content):
    """Calculate the longest palindromic subsequence in text content."""
    # Preprocess the content.
    text = content.lower()
    text = re.sub("[^a-zA-Z]", "", text)  # Remove non-alphabetic characters.

    current_max = 0
    if (
        not content
    ):  # If the string is empty, then the longest palindrome is 0 characters long.
        return 0
    else:  # If the string is at least 1 character long, then the longest palindrome is 1 characters long.
        current_max += 1

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j : i + 1]

            if chunk == chunk[::-1] and len(chunk) > current_max:
                current_max = len(chunk)

    return current_max
