# Binary Search
# Standard binary search algorithm, (Divide and Conquer)
def binary_search(self, nums: List[int], target: int) -> int:
    lo = 0
    hi = len(nums)-1
    while lo <= hi:
        mid = lo + (hi-lo//2)
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            hi = mid-1
        else: # target > nums[mid]
            lo = mid+1
    return -1 # no index found