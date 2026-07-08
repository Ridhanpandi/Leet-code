// Last updated: 08/07/2026, 20:48:33
import java.util.*;

class Solution {
    public String countOfAtoms(String formula) {
        int i = 0;
        int n = formula.length();

        Stack<Map<String, Integer>> stack = new Stack<>();
        stack.push(new HashMap<>());

        while (i < n) {
            char c = formula.charAt(i);

            if (c == '(') {
                stack.push(new HashMap<>());
                i++;
            } 
            else if (c == ')') {
                Map<String, Integer> top = stack.pop();
                i++;

                int start = i;
                int multiplier = 1;

                while (i < n && Character.isDigit(formula.charAt(i))) {
                    i++;
                }

                if (start < i) {
                    multiplier = Integer.parseInt(formula.substring(start, i));
                }

                Map<String, Integer> peek = stack.peek();
                for (String key : top.keySet()) {
                    peek.put(key, peek.getOrDefault(key, 0) + top.get(key) * multiplier);
                }
            } 
            else {
                int start = i;
                i++; // uppercase letter

                while (i < n && Character.isLowerCase(formula.charAt(i))) {
                    i++;
                }

                String name = formula.substring(start, i);

                start = i;
                while (i < n && Character.isDigit(formula.charAt(i))) {
                    i++;
                }

                int count = 1;
                if (start < i) {
                    count = Integer.parseInt(formula.substring(start, i));
                }

                Map<String, Integer> top = stack.peek();
                top.put(name, top.getOrDefault(name, 0) + count);
            }
        }

        Map<String, Integer> result = stack.pop();

        List<String> keys = new ArrayList<>(result.keySet());
        Collections.sort(keys);

        StringBuilder sb = new StringBuilder();
        for (String key : keys) {
            sb.append(key);
            if (result.get(key) > 1) {
                sb.append(result.get(key));
            }
        }

        return sb.toString();
    }
}