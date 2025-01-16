
def single_number(nums: list)-> int:
    freq = {}

    for num in nums:
        if num in freq.keys():
            freq[num] +=1
        else:
            freq[num] = 1
    for num, count in freq.items():
        if count == 1:
            return num
if __name__ == '__main__':
    nums = [4,1,1,3,4,2,3]
    print(single_number(nums))