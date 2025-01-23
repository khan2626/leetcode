"""
it reverses an integer within 32 bits
I
nput: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

"""


def reverse_int(x):

    MAX_INT = 2 ** 31 -1
    MIN_INT = -2 ** 31

    reverse = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x != 0:
        if reverse > MAX_INT/10 or reverse < MIN_INT/10:
            return 0
        digit = x % 10
        reverse = reverse * 10 + digit
        x = x // 10
    return sign * reverse

if __name__ == '__main__':
    x = 1563847412
    print(reverse_int(x))