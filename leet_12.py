
def serch_insert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

if __name__ == '__main__':
    nums = [1, 2, 4, 5, 7]
    print(serch_insert(nums, 10))