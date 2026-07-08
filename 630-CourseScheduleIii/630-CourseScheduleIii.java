// Last updated: 08/07/2026, 20:48:40
import java.util.*;

class Solution {
    public int scheduleCourse(int[][] courses) {
        
        // Step 1: sort by lastDay (deadline)
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);

        // max heap to store durations
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        int time = 0;

        for (int[] course : courses) {
            int duration = course[0];
            int lastDay = course[1];

            time += duration;
            maxHeap.offer(duration);

            // if we exceed deadline, remove longest course
            if (time > lastDay) {
                time -= maxHeap.poll();
            }
        }

        return maxHeap.size();
    }
}