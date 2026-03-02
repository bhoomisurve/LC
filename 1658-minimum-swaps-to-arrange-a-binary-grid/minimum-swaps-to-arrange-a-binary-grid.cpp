class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> rightMost(n);

        for (int i = 0; i < n; i++) {
            int pos = -1;
            for (int j = n - 1; j >= 0; j--) {
                if (grid[i][j] == 1) {
                    pos = j;
                    break;
                }
            }
            rightMost[i] = pos;
        }

        int swaps = 0;

        for (int i = 0; i < n; i++) {

            int j = i;
            while (j < n && rightMost[j] > i)
                j++;

            if (j == n) return -1;

            while (j > i) {
                swap(rightMost[j], rightMost[j - 1]);
                swaps++;
                j--;
            }
        }

        return swaps;
    }
};