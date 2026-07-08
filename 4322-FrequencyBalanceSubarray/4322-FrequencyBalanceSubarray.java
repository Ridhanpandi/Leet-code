// Last updated: 08/07/2026, 20:48:20
class Solution {
    public int getLength(int[] nums) {
        int n = nums.length;
        int ans = 1;

        for (int i = 0; i < n; i++) {
            HashMap<Integer, Integer> cnt = new HashMap<>();
            HashMap<Integer, Integer> freqCnt = new HashMap<>();

            for (int j = i; j < n; j++) {
                int x = nums[j];

                int oldFreq = cnt.getOrDefault(x, 0);

                if (oldFreq > 0) {
                    freqCnt.put(oldFreq, freqCnt.get(oldFreq) - 1);
                    if (freqCnt.get(oldFreq) == 0) {
                        freqCnt.remove(oldFreq);
                    }
                }

                int newFreq = oldFreq + 1;
                cnt.put(x, newFreq);
                freqCnt.put(newFreq, freqCnt.getOrDefault(newFreq, 0) + 1);

                boolean valid = false;

                if (cnt.size() == 1) {
                    valid = true;
                } else if (freqCnt.size() == 2) {
                    Iterator<Integer> it = freqCnt.keySet().iterator();

                    int a = it.next();
                    int b = it.next();

                    int small = Math.min(a, b);
                    int large = Math.max(a, b);

                    valid = (large == 2 * small);
                }

                if (valid) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
        }

        return ans;
    }
}