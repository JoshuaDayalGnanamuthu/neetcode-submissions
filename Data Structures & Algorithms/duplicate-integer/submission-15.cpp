#include <set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> counter; // Better than just set (uses an has implementation (.find time complexity is O(1) avg case, O(n) worst case))
        for (int &num: nums) {
            if (counter.find(num) != counter.end()) {
                return true;
            }
            else {
                counter.insert(num);
            }
        }
        return false;
    }
};