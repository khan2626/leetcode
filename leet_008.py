from typing import List
def three_sum_closest(num: List, target: int) -> int :

    sorted_num = sorted(num)
    closest_sum = float('inf')
    

    for i in range(len(sorted_num)):
        j = i + 1
        k = len(sorted_num) - 1

        while j < k:
            current_sum = sorted_num[i] + sorted_num[j] + sorted_num[k]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                j += 1
            elif current_sum > target:
                k -= 1
            else:
                return current_sum
    return closest_sum

if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print(three_sum_closest(nums, target)) #output: 2

    nums = [0, 0, 0, 0]
    target = 1
    result = three_sum_closest(nums, target)
    print(result)  # Output: 2
