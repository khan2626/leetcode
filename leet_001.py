#!/usr/bin/python3
"""
return the longest possible substring of palindrom
from a string
"""

def longest_palindrome_substr(s: str):

    max_str = s[0]
    max_len = 1

    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            if j - i + 1 > max_len and s[i : j + 1] == s[i : j+1][::-1]:
                max_str = s[i : j + 1]
                max_len = j - i + 1
    return(max_len, max_str)

if __name__ == '__main__':
    print(longest_palindrome_substr('aaabz'))
