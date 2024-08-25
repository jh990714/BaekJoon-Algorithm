import java.util.*;

class Solution {
    List<Integer>[] graph;
    int[] visited;
    
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        graph = new ArrayList[n+1];
        
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int[] road : roads) {
            graph[road[0]].add(road[1]);
            graph[road[1]].add(road[0]);
        }
        
        visited = new int[n+1];
        Arrays.fill(visited, -1);
        
        bfs(destination);
        
        int[] result = new int[sources.length];
        for (int i = 0; i < sources.length; i++) {
            result[i] = visited[sources[i]];
        }
        
        return result;
    }
    
    public void bfs(int start) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        visited[start] = 0;
        
        while (!q.isEmpty()) {
            int node = q.poll();
            
            for (int nextNode : graph[node]) {
                if (visited[nextNode] != -1) continue;
                
                visited[nextNode] = visited[node] + 1;
                q.add(nextNode);
            }
        }
    }
}
