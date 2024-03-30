class Solution {
public:
    int SlidingWindow(vector<int>& nums, int k) {
        int left = 0, right = 0, ans = 0;
        unordered_map<int,int> check;
        while (right < nums.size())
        {
            check[nums[right]]++;
            while (check.size() > k){
                check[nums[left]]--;
                if(check[nums[left]] == 0)
                check.erase(nums[left]);
                left++;
            }
            ans+= right - left +1;
            right++;
        }
        return ans;
    }


    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return SlidingWindow(nums,k) - SlidingWindow(nums, k-1);
    }
};