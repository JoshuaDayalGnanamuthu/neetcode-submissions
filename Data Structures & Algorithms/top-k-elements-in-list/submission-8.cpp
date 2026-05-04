#include <algorithm>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, vector<int>> counter;
        vector<int> seen;
        vector<int> result;

        for (int& num: nums) {
            if (find(seen.begin(), seen.end(), num) != seen.end()) continue;
            else {
                int count = std::count(nums.begin(), nums.end(), num);
                counter[count].push_back(num);
                seen.push_back(num);
            }
        }
        
        for (map<int, vector<int>>::reverse_iterator it = counter.rbegin(); it != counter.rend(); ++it) {
            for (int num: it->second) {
                if (k == 0) return result;
                result.push_back(num);
                k -= 1;
            }
        }
    }
};
