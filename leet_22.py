
def pascal_triangle_ii(index_row: int):

    res = [[1]]

    for _ in range(index_row):
        dummy_row = [0] + res[-1] + [0]
        row = []
        for i in range(len(res[-1]) + 1):
            row.append(dummy_row[i] + dummy_row[i+1])
        res.append(row)
    return res[-1]
if __name__ == '__main__':
    print(pascal_triangle_ii(3))