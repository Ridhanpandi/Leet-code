// Last updated: 08/07/2026, 20:48:53
import java.util.*;

class Solution {
    public String[] findRelativeRanks(int[] score) {
        int n = score.length;
        
        // Step 1: Pair score with index
        int[][] arr = new int[n][2]; // [score, index]
        
        for (int i = 0; i < n; i++) {
            arr[i][0] = score[i];
            arr[i][1] = i;
        }
        
        // Step 2: Sort by score descending
        Arrays.sort(arr, (a, b) -> b[0] - a[0]);
        
        // Step 3: Result array
        String[] result = new String[n];
        
        // Step 4: Assign ranks
        for (int i = 0; i < n; i++) {
            int idx = arr[i][1];
            
            if (i == 0) {
                result[idx] = "Gold Medal";
            } else if (i == 1) {
                result[idx] = "Silver Medal";
            } else if (i == 2) {
                result[idx] = "Bronze Medal";
            } else {
                result[idx] = String.valueOf(i + 1);
            }
        }
        
        return result;
    }
}