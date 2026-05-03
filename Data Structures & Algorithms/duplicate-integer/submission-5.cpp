#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> occourances;

        for (int &i: nums) {
            occourances[i]++;
        }

        for (auto pair: occourances){
            if (pair.second > 1) return true;
        }

        return false;

        
    }
};