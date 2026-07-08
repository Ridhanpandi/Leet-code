// Last updated: 08/07/2026, 20:49:03
class Solution {
    public int splitArray(int[] nums, int k) {
        int n = nums.length;
        if(k > n) return -1;

        int maxi = Integer.MIN_VALUE;
        int sum = 0;

        for(int num : nums) {
            maxi = Math.max(maxi, num);
            sum += num;
        }

        int low = maxi;
        int high = sum;

        while(low <= high) {
            int mid = low + (high - low) / 2;
            int partitions = countPartitions(nums, mid);

            if(partitions > k) low = mid + 1;
            else high = mid - 1; 
        }

        return low;
    }
    public static int countPartitions(int[] nums, int maxSum) {
        int n = nums.length;
        int partitions = 1;
        int subarraySum = 0;

        for(int i=0; i<n; i++) {
            if(subarraySum + nums[i] <= maxSum) {
                subarraySum += nums[i];
            } else {
                partitions++;
                subarraySum = nums[i];
            }
        }

        return partitions;
    }
}