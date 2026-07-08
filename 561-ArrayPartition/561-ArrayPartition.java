// Last updated: 08/07/2026, 20:48:48
import java.util.*;

class Solution {
    public int arrayPairSum(int[] nums) {
        // Step 1: sort the array
        Arrays.sort(nums);

        int sum = 0;

        // Step 2: take every even-indexed element
        // (0,2,4...) since they are mins of pairs
        for (int i = 0; i < nums.length; i += 2) {
            sum += nums[i];
        }

        return sum;
    }
}