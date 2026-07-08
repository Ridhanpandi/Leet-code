// Last updated: 08/07/2026, 20:49:37
import java.util.*;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {

        List<int[]> events = new ArrayList<>();

        for (int[] b : buildings) {
            // Start event
            events.add(new int[]{b[0], -b[2]});

            // End event
            events.add(new int[]{b[1], b[2]});
        }

        Collections.sort(events, (a, b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(a[1], b[1]);
        });

        List<List<Integer>> result = new ArrayList<>();

        TreeMap<Integer, Integer> heights = new TreeMap<>();
        heights.put(0, 1);

        int prevMax = 0;

        for (int[] event : events) {

            int x = event[0];
            int h = event[1];

            if (h < 0) {
                // Building starts
                h = -h;
                heights.put(h, heights.getOrDefault(h, 0) + 1);
            } else {
                // Building ends
                heights.put(h, heights.get(h) - 1);

                if (heights.get(h) == 0) {
                    heights.remove(h);
                }
            }

            int currMax = heights.lastKey();

            if (currMax != prevMax) {
                result.add(Arrays.asList(x, currMax));
                prevMax = currMax;
            }
        }

        return result;
    }
}