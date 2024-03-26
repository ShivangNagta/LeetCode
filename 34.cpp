class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = -1;
        int last = -1;
        int start = 0;
        int end = nums.size() -1;
        
        while (start<=end)
        {
            int mid = ((end-start)>>1) + start;
            if (nums[mid] == target)
            {
                first = mid;
                end = mid -1;
            }
            else if ( nums[mid] < target)
            {
                start = mid + 1;
            }
            else if (nums[mid] > target)
            {
                end = mid -1;
            }


        }
        start = 0;
        end = nums.size() -1;        

        while (start<=end)
        {
            int mid = ((end-start)>>1)+start;
            if (nums[mid] == target)
            {
                last = mid;
                start = mid +1;
            }
            else if ( nums[mid] < target)
            {
                start = mid + 1;
            }
            else if (nums[mid] > target)
            {
                end = mid -1;
            }

        }

        vector<int>a(2);
        a[0] = first;
        a[1] = last;
        return a;
    }
};