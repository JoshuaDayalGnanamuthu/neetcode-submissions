class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> counter;
        for (int &num: nums) {
            if (counter[num]) return true;
            else counter[num]++;
        }
        return false;
    }
};