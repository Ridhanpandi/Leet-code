// Last updated: 17/07/2026, 14:43:27
1public class Solution {
2    public String multiply(String num1, String num2) {
3        int n1 = num1.length(), n2 = num2.length();
4        int[] products = new int[n1 + n2];
5        for (int i = n1 - 1; i >= 0; i--) {
6            for (int j = n2 - 1; j >= 0; j--) {
7                int d1 = num1.charAt(i) - '0';
8                int d2 = num2.charAt(j) - '0';
9                products[i + j + 1] += d1 * d2;
10            }
11        }
12        int carry = 0;
13        for (int i = products.length - 1; i >= 0; i--) {
14            int tmp = (products[i] + carry) % 10;
15            carry = (products[i] + carry) / 10;
16            products[i] = tmp;
17        }
18        StringBuilder sb = new StringBuilder();
19        for (int num : products) sb.append(num);
20        while (sb.length() != 0 && sb.charAt(0) == '0') sb.deleteCharAt(0);
21        return sb.length() == 0 ? "0" : sb.toString();
22    }
23}