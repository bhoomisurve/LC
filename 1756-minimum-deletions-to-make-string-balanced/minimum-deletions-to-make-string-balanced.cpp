class Solution {
public:
    int minimumDeletions(string s) {
        int del = 0;
        int b = 0;
        for (char c : s){
            if (c == 'b'){
                ++b;
            } else {
                del = min(del + 1, b);
            }
        }
        return del;
    }
};