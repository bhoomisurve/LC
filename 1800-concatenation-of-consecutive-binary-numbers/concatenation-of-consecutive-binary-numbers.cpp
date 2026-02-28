class Solution {
public:
    int concatenatedBinary(int n) {
        const int mod = 1000000007;
        long result = 0; 
        for (int i = 1; i <= n; ++i) {
            int bitLength = 32 - __builtin_clz(i);
            result = ((result << bitLength) | i) % mod;
        }
        return static_cast<int>(result);
    }
};