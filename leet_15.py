
def plus1(digits):

    for i in range(len(digits)-1, -1, -1):
        if digits[i] +1 != 10:
            digits[i] +=1
            return digits
        digits[i] = 0
    return digits

if __name__ == "__main__":
    digits = [1, 2, 3, 9, 9]
    print(plus1(digits))