class Solution {
public:
    bool canBeEqual(string s1, string s2) {
        multiset<char> a{ s1[0], s1[2] }, b{ s1[1], s1[3] };
        multiset<char> c{ s2[0], s2[2] }, d{ s2[1], s2[3] };
        return a == c && b == d;
    }
};