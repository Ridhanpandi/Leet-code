// Last updated: 08/07/2026, 20:49:18
class Solution {

    private int[] count;
    private int[] index;
    private int[] tempIndex;

    public List<Integer> countSmaller(int[] nums) {

        int n = nums.length;

        count = new int[n];
        index = new int[n];
        tempIndex = new int[n];

        for (int i = 0; i < n; i++) {
            index[i] = i;
        }

        mergeSort(nums, 0, n - 1);

        List<Integer> result = new ArrayList<>();

        for (int c : count) {
            result.add(c);
        }

        return result;
    }

    private void mergeSort(int[] nums, int left, int right) {

        if (left >= right)
            return;

        int mid = left + (right - left) / 2;

        mergeSort(nums, left, mid);
        mergeSort(nums, mid + 1, right);

        merge(nums, left, mid, right);
    }

    private void merge(int[] nums, int left, int mid, int right) {

        int i = left;
        int j = mid + 1;
        int k = left;

        int rightCount = 0;

        while (i <= mid && j <= right) {

            if (nums[index[j]] < nums[index[i]]) {

                tempIndex[k++] = index[j++];
                rightCount++;

            } else {

                count[index[i]] += rightCount;
                tempIndex[k++] = index[i++];
            }
        }

        while (i <= mid) {
            count[index[i]] += rightCount;
            tempIndex[k++] = index[i++];
        }

        while (j <= right) {
            tempIndex[k++] = index[j++];
        }

        for (int p = left; p <= right; p++) {
            index[p] = tempIndex[p];
        }
    }
}