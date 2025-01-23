

def zigzag(s, numRows: int):
    step = -1
    idx = 0

    if numRows > len(s):
        return s
    
    rows = [[] for row in range(numRows)]
    for char in s:
        rows[idx].append(char)
        if idx == 0:
            step += 1
        elif idx == numRows -1:
            step -= 1
        idx += step

    for i in range(numRows):
        rows[i] = "".join(rows[i])
    return "".join(rows)

if __name__ == '__main__':
    s = "helloworld"
    numRows = 4
    print(zigzag(s, numRows))