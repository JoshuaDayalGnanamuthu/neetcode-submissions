#include <algorithm>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> counter;
        std::vector<int> results;

        for (const int &num: nums) {
            counter[num]++;
        }

        std::vector<vector<int>> frequencies (nums.size());

        for (auto pair: counter) {
            frequencies[pair.second - 1].push_back(pair.first);
        }

        
        for ( int i = nums.size() - 1; i >= 0; --i ) {
            for (int num: frequencies[i]) {
                if (k == 0) return results;
                else {
                    results.push_back(num);
                    k--;
                }
            }
        }
        
        return results;
    }
};
