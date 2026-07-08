// Last updated: 08/07/2026, 20:48:32
class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> dead = new HashSet<>(Arrays.asList(deadends));
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();

        String start = "0000";

        if (dead.contains(start)) return -1;
        if (start.equals(target)) return 0;

        queue.add(start);
        visited.add(start);
        int turns = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            turns++;

            for (int i = 0; i < size; i++) {
                String curr = queue.poll();

                // Try turning each of 4 wheels, in both directions
                for (int w = 0; w < 4; w++) {
                    for (int dir : new int[]{1, -1}) {
                        char[] chars = curr.toCharArray();
                        chars[w] = (char)((chars[w] - '0' + dir + 10) % 10 + '0');
                        String next = new String(chars);

                        if (next.equals(target)) return turns;

                        if (!visited.contains(next) && !dead.contains(next)) {
                            visited.add(next);
                            queue.add(next);
                        }
                    }
                }
            }
        }

        return -1;
    }
}