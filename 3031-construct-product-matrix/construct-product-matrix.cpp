class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        int mod = 12345;
        int n = grid.size();
        int m = grid[0].size();
        int size = n * m;

        vector<int> arr(size);
        int index = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[index++] = grid[i][j] % mod;
            }
        }

        vector<int> prefix(size), result(size);
        prefix[0] = 1;

        for (int i = 1; i < size; i++) {
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % mod;
        }

        int suffix = 1;

        for (int i = size - 1; i >= 0; i--) {
            result[i] = (prefix[i] * suffix) % mod;
            suffix = (suffix * arr[i]) % mod;
        }

        vector<vector<int>> ans(n, vector<int>(m));
        index = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ans[i][j] = result[index++];
            }
        }

        return ans;
    }
};