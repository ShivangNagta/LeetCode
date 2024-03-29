class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr)  - 1
        while(start<=end):
            mid = (start + end)//2
            if mid == 0:
                if arr[mid] > arr[mid+1]:
                    return mid
                else:
                    start = mid+1
            else:
                if (arr[mid] > arr[mid-1]) and arr[mid] > arr[mid+1] : return mid
                elif arr[mid] > arr[mid-1]:
                    start = mid+1
                else:
                    end = mid -1
        return mid
        