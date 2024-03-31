class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long count = 0;
        int badi = -1, mini = -1, maxi = -1;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] < minK || nums[i] > maxK) badi = i;
            if (nums[i] == minK) mini = i;
            if (nums[i] == maxK) maxi = i;
            count += max(0, min(mini,maxi) - badi);
        }

        return count;     
    }
};