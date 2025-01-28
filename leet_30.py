"""
it returns a string in a zigzag pattern.
s = string
numRows = number of rows

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
"""

def zigzag(s: str, numRows: int):
    
    if numRows >= len(s) or numRows == 1:
        return s
    step = 1
    idx = 0
    rows = [[] for row in range(numRows)]
    for char in s:
        rows[idx].append(char)
        if idx == 0:
            step = 1
        elif idx == numRows -1:
            step = -1
        idx += step

    for i in range(numRows):
        rows[i] = "".join(rows[i])
    return "".join(rows)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    print(zigzag(s, numRows))