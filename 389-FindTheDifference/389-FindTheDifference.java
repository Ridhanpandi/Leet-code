// Last updated: 08/07/2026, 20:49:05
class Solution {
    public char findTheDifference(String s, String t) {

        char result = 0;

        for (char c : s.toCharArray()) {
            result ^= c;
        }

        for (char c : t.toCharArray()) {
            result ^= c;
        }

        return result;
    }
}