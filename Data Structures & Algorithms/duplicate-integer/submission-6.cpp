#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> occourances;

        for (int &num: nums) {
            if (occourances.count(num)) return true;
            occourances.insert(num);
        } 
        
        return false;

        
    }
};