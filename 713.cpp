class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k<=1) return 0;
        int start = 0, end = 0, product = 1, ans = 0;
        while (end < nums.size())
        {
            product *= nums[end];
            while (product >= k)
            {
                product /= nums[start];
                start += 1;
            } 
            ans += end - start + 1;
            end += 1;
            
        }
        return ans;
    }
};