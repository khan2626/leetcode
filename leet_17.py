

def mysqrt(x):
    start = 0
    end = x

    while start <= end:
        mid = (start + end) // 2
        if mid * mid > x:
            end = mid - 1
        elif mid * mid < x:
            start +=1
        else:
            return mid
    return end

if __name__ == '__main__':
    x = 7
    print(mysqrt(x))