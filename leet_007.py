from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    sorted_nums = sorted(nums)
    result = []

    for i in range(len(sorted_nums)):
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
            continue
        j = i + 1
        k = len(sorted_nums) - 1

        while j < k:
            sum = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]

            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                j += 1
                while sorted_nums[j] == sorted_nums[j - 1]:
                    j += 1
    return result

if __name__ == '__main__':
    arr = [-1,0,1,2,-1,-4]
    print(three_sum(arr))
