def merge_sorted_arr(nums1, m, nums2, n):
    midx = m-1
    nidx = n-1
    end = (m+n) -1

    while nidx >= 0:
        if midx >= 0 and nums1[midx] > nums2[nidx]:
            nums1[end] = nums1[midx]
            midx -= 1
        else:
            nums1[end] = nums2[nidx]
            nidx -=1
        end -=1
    return nums1

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m=3
    n=3
    print(merge_sorted_arr(nums1, m, nums2, n))