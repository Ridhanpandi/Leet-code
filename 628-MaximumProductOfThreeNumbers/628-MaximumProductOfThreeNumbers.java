// Last updated: 08/07/2026, 20:48:42
import java.util.*;

class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;

        // Case 1: 3 largest numbers
        int max1 = nums[n - 1] * nums[n - 2] * nums[n - 3];

        // Case 2: 2 smallest (negative) + largest
        int max2 = nums[0] * nums[1] * nums[n - 1];

        return Math.max(max1, max2);
    }
}