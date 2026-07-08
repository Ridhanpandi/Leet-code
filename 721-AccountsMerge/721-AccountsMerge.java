// Last updated: 08/07/2026, 20:48:35
import java.util.*;

class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        int n = accounts.size();

        UnionFind uf = new UnionFind(n);

        Map<String, Integer> emailToAccount = new HashMap<>();

        for (int i = 0; i < n; i++) {
            List<String> account = accounts.get(i);

            for (int j = 1; j < account.size(); j++) {
                String email = account.get(j);

                if (!emailToAccount.containsKey(email)) {
                    emailToAccount.put(email, i);
                } else {
                    uf.union(i, emailToAccount.get(email));
                }
            }
        }

        Map<Integer, TreeSet<String>> groups = new HashMap<>();

        for (String email : emailToAccount.keySet()) {
            int accountIndex = emailToAccount.get(email);
            int parent = uf.find(accountIndex);

            groups.putIfAbsent(parent, new TreeSet<>());
            groups.get(parent).add(email);
        }

        List<List<String>> result = new ArrayList<>();

        for (int parent : groups.keySet()) {
            List<String> merged = new ArrayList<>();

            merged.add(accounts.get(parent).get(0)); // name
            merged.addAll(groups.get(parent));

            result.add(merged);
        }

        return result;
    }
}

class UnionFind {
    int[] parent;

    public UnionFind(int n) {
        parent = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int a, int b) {
        parent[find(a)] = find(b);
    }
}