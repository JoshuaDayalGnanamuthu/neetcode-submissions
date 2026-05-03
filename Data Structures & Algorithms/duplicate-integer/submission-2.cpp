#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> occourances;

        for (int &x: nums) occourances[x]++;

        for (auto &pair: occourances){
            if (pair.second > 1) return true;
        }
        return false;

    }
};
