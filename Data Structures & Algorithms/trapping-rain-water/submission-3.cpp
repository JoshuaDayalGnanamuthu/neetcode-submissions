class Solution {
public:
    int trap(vector<int>& height) {
        int result = 0;
        int left_max = 0; int right_max = 0;
        int *left_pointer = &height[0];
        int *right_pointer = &height[0] + height.size() - 1;

        while (left_pointer < right_pointer ){
            left_max = max(left_max, *left_pointer);
            right_max = max(right_max, *right_pointer);

            if (left_max < right_max){
                result += left_max - *left_pointer;
                left_pointer++;
            }

            else {
                result += right_max - *right_pointer;
                right_pointer--;
            }
        }
        return result;
    }
};