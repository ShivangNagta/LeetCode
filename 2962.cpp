class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long left = 0, right = 0, countMax = 0, ans = 0;
        long long maxElement = *max_element(nums.begin(), nums.end());
        while (right < nums.size())
        {
            if (nums[right] == maxElement) countMax++;
            while (countMax >= k)
            {
                ans += nums.size() - right;
                if (nums[left] == maxElement) countMax--;
                left++;
            }
            right++;
        }
        return ans;
    }
};