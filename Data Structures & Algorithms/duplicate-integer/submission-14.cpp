#include <set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> counter;
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