#!/usr/bin/python3

def len_possible_substr(s: str) -> str:
    left = 0
    new_str = set()
    max_len = 0
    

    for right in range(len(s)):
        while s[right] in new_str:
            new_str.remove(s[left])
            left += 1
        new_str.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == '__main__':
    print(len_possible_substr('abcabcbb'))
    print(len_possible_substr('bbbb'))
