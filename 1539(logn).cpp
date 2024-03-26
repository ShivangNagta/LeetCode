class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int start = 0, end = arr.size() - 1, mid;
        while (start <= end)
        {
            mid = start + ((end-start)/2);
            int missing = arr[mid] -mid -1;
            if (missing < k)
            start = mid +1;
            else
            end = mid - 1;
        }
        return end + k + 1;
    }
};