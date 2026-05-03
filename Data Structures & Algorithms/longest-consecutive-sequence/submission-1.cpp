class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (!nums.size()) return 0;
        set<int> list;
        
        for (int num: nums) list.insert(num);
        int counter = 1;
        int output = 1;

        for (int i: list){
            if (list.count(i + 1)){
                counter++;
            }
            else {
                if (counter > output) output = counter;
                counter = 1;
            }
        }
        return output;
        
    }
};
