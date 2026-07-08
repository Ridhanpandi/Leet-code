// Last updated: 08/07/2026, 20:49:10
import java.util.*;

class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {

        int n = nums.length;
        Arrays.sort(nums);

        int[] dp = new int[n];
        int[] parent = new int[n];

        Arrays.fill(dp, 1);

        int maxLen = 1;
        int maxIndex = 0;

        for (int i = 0; i < n; i++) {

            parent[i] = i;

            for (int j = 0; j < i; j++) {

                if (nums[i] % nums[j] == 0 &&
                    dp[j] + 1 > dp[i]) {

                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }

            if (dp[i] > maxLen) {
                maxLen = dp[i];
                maxIndex = i;
            }
        }

        List<Integer> result = new ArrayList<>();

        while (parent[maxIndex] != maxIndex) {
            result.add(nums[maxIndex]);
            maxIndex = parent[maxIndex];
        }

        result.add(nums[maxIndex]);

        Collections.reverse(result);

        return result;
    }
}