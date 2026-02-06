class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        int maxlen = 1;
        int i = 0;
        for (int j = 0; j < n; j++){
            while ((long long)nums[j] > (long long)k * nums[i]){
                i++;
            }
            maxlen = max(maxlen, j - i + 1);
        }
        return n - maxlen;
    }
};