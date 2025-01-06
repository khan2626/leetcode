def first_occurence_index(haystack: str, needle: str):

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if __name__ == '__main__':
    haystack = 'sadbutcat'
    needle = 'sad'
    print(first_occurence_index(haystack, needle))