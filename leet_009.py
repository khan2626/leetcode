

def no_duplicate(nums: int):
    replace = 1
    count = 1
    numbers = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:   
            replace = nums[i]
            numbers.append(replace)
            count += 1
    print(count, "-->", numbers)


if __name__ == "__main__":
    nums = [0,0,0,1,1,2,3,3,3,4,4]
    no_duplicate(nums)