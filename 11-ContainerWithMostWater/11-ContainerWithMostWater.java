// Last updated: 08/07/2026, 20:50:49
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxWater = 0;

        while (left < right) {
            int h = Math.min(height[left], height[right]);
            int w = right - left;
            maxWater = Math.max(maxWater, h * w);

            // Move the shorter wall inward
            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxWater;
    }
}