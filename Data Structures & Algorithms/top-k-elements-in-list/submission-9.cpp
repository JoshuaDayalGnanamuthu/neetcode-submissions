#include <algorithm>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        std::map<int, std::vector<int>> counter;
        std::unordered_set<int> seen;

        for (int &num: nums) {
            if (!seen.count(num)) {
                counter[std::count(nums.begin(), nums.end(), num)].push_back(num);
                seen.insert(num);
            }
            
        }
    
        while (k) {
            for (auto cit = counter.crbegin(); cit != counter.crend(); ++cit){
                for (const int &ele: cit->second) {
                    if (k == 0) return result;
                    else {
                        result.push_back(ele);
                        k--;
                    }
                }
            }
        }
    }
};
