// Last updated: 08/07/2026, 20:50:55
class Solution {
    public int reverse(int x) {
        long reversed = 0;
        boolean negative = x < 0;
        long num = Math.abs((long) x);
        
        while (num != 0) {
            int digit = (int)(num % 10);
            num /= 10;
            reversed = reversed * 10 + digit;
        }
        
        if (negative) reversed = -reversed;
        
        if (reversed > Integer.MAX_VALUE || reversed < Integer.MIN_VALUE) return 0;
        
        return (int) reversed;
    }
}

