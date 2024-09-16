#!/usr/bin/python3

"""
return a boolean if an integer is a palindrome
"""

def is_palindrome(num: int) -> bool:
    original_num = num
    reversed = 0

    if num < 0:
        return False
    
    while num > 0:
        digit = num % 10
        reversed = reversed * 10 + digit
        num //= 10
    
    return reversed == original_num
    

if __name__ == '__main__':
    print(is_palindrome(123))
    print(is_palindrome(121))
    print(is_palindrome(1010))
    print(is_palindrome(101))