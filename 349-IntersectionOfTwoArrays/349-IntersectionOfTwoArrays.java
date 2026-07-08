// Last updated: 08/07/2026, 20:49:13
        class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> result = new HashSet<>();
        for (int n : nums1) {
            set1.add(n);
        }

        for (int n : nums2) {
            if (set1.contains(n)) {
                result.add(n); 
            }
        }
        int[] arr = new int[result.size()];
        int i = 0;
        for (int n : result) {
            arr[i++] = n;
        }
        return arr;
    }
}
        