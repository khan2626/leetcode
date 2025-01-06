

def valid_parentheses(s):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []

    for bracket in s:
        if bracket in pairs.keys():
            stack.append(bracket)
        elif len(stack) == 0 or pairs[stack.pop()] != bracket:
            return False
    # if len(stack) == 0:
    #     return True
    # else: 
    #     return False
    return len(stack) == 0

if __name__ == '__main__':
    s = "[{()}]"
    print(valid_parentheses(s))
        
