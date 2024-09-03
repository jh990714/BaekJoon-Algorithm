import java.util.*;

class Solution {
    private List<String> results;
    private boolean[] visited;
        
    public String[] solution(String[][] tickets) {
        results = new ArrayList<>();
        visited = new boolean[tickets.length];
        
        dfs(tickets, "ICN", "ICN", 0);
        
        Collections.sort(results);
        
        return results.get(0).split(" ");
    }
    
    private void dfs(String[][] tickets, String cur, String path, int count) {
        if (count == tickets.length) {
            results.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && tickets[i][0].equals(cur)) {
                visited[i] = true;
                dfs(tickets, tickets[i][1], path + " " + tickets[i][1], count + 1);
                
                visited[i] = false;
            }
        }
    }
}