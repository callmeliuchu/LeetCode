class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size() - 1;
        int c = 0;
        while(i<j){
            int h = min(height[i],height[j]);
            int w = j - i;
            c = max(c,h*w);
            while(height[i]<=h && i<j){
                i++;
            }
            while(height[j]<=h && i<j){
                j--;
            }
        }
        return c;
    }
};