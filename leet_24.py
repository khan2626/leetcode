
def valid_palindrome(s: str):
    s = "".join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(s) -1

    while left <= right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

if __name__ == '__main__':
    s = 'race a car'
    s1 = "A man, a plan, a canal: Panama"
    print(valid_palindrome(s))
    print(valid_palindrome(s1))