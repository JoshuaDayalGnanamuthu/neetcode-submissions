class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
       unordered_set<int> duplicates;
       for (int number : nums) {
        if (duplicates.count(number)){
            return true;
        }
        duplicates.insert(number);
       }
       return false; 
    }
};