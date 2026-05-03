#include<algorithm>
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int area = 0;
        int* left_pointer = &heights[0];
        int* right_pointer = &heights[0] + heights.size() - 1;

        while (left_pointer < right_pointer) {
            int amount = min(*left_pointer, *right_pointer) * (right_pointer - left_pointer);
            if (amount > area) area = amount;

            if (*left_pointer > *right_pointer) right_pointer--;
            else left_pointer++;
        }

        return area;
        
    }
};
