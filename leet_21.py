
def pascal_triangle(num_rows: int):
    res = [[1]]

    for _ in range(num_rows - 1):
        dummy_row = [0] + res[-1] + [0]
        row = []
        for i in range(len(res[-1]) + 1):
            row.append(dummy_row[i] + dummy_row[i+1])
        res.append(row)
    return res
if __name__ == '__main__':
    print(pascal_triangle(5))