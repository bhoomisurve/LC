class Solution {
public:
    int mySqrt(int x) {
        int res = 1;
        while (res <= x / res){
            res += 1;

        }
        return res - 1;
    }
};