
def max_area(height):
    maxArea = 0
    l = 0
    r = len(height) -1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        if height[l] < height[r]:
            l +=1
        else:
            r -=1
    return maxArea

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(max_area(height))