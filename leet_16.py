

def add_binary(a, b):
    idxa = len(a) - 1
    idxb = len(b) - 1
    carry = 0
    res = []

    
    while idxa >= 0 or idxb >= 0 or carry == 1:
        if idxa >= 0:
            carry += int(a[idxa])
            idxa -=1
        if idxb >= 0:
            carry += int(b[idxb])
            idxb -= 1

        res.append(str(carry % 2))
        carry = carry // 2
    return "".join(res)[::-1]
if __name__ == "__main__":
    a = "11"
    b = "1"
    print(add_binary(a, b))
            
