class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int left = 0, right = 0; 
        int ans = 1;
        map<int,int> repCheck;
        int n = nums.size();
        while (left < n && right < n){
            repCheck[nums[right]] +=1;
            while (repCheck[nums[right]] > k){
                repCheck[nums[left]] -=1;
                left+=1;
            }
            ans = max(ans, right- left +1);
            right+=1;
        }
        return ans;      
    }
};