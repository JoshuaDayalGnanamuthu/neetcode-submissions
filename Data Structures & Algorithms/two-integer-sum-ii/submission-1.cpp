class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
       int* left_pointer = &numbers[0];
       int* right_pointer = &numbers[0] + numbers.size() - 1;

       while (*left_pointer < *right_pointer) {
        if (target == *left_pointer + *right_pointer){
            cout << *left_pointer << *right_pointer;
            int left_index  = left_pointer  - &numbers[0] + 1;
            int right_index = right_pointer - &numbers[0] + 1;
            return {left_index, right_index};
        }
        else if (target - *left_pointer < * right_pointer){
            right_pointer--;
        }
        else{
            left_pointer++;
        }
       }
       return {};
    }
};
