def length_of_last_word(s):
    end = len(s) -1

    while s[end] == " ":
        end -= 1
    start = end
    while s[start] != " ":
        start -= 1
    
    return end - start

if __name__ == '__main__':
    s = "hello world   "
    print(length_of_last_word(s))