// Last updated: 08/07/2026, 20:48:57
import java.util.*;

class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);

        int child = 0;
        int cookie = 0;

        while (child < g.length && cookie < s.length) {
            if (s[cookie] >= g[child]) {
                child++; // child is satisfied
            }
            cookie++; // move to next cookie
        }

        return child;
    }
}