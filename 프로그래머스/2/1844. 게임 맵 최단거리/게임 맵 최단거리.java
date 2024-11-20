import java.util.*;

class Solution {
    private int[][] visited;
    private int[] dx = {1, 0, -1, 0};
    private int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        visited = new int[maps.length][maps[0].length];
        
        bfs(maps, 0, 0);
        
        int answer = visited[maps.length-1][maps[0].length-1];
        
        return answer == 0 ? -1 : answer;
    }
    
    private void bfs(int[][] maps, int x, int y) {
        Queue<int[]> que = new LinkedList<>();
        que.offer(new int[]{x, y});
        
        visited[x][y] = 1;
        
        while (!que.isEmpty()) {
            int[] point = que.poll();
            int cx = point[0];
            int cy = point[1];
            
            if (cx == maps.length && cy == maps[0].length) {
                return;
            }
            
            for (int i = 0; i < dx.length; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                
                if (nx < 0 || nx >= maps.length || ny < 0 || ny >= maps[0].length) continue;
                if (visited[nx][ny] != 0) continue;
                if (maps[nx][ny] == 0) continue;
                
                visited[nx][ny] = visited[cx][cy] + 1;
                que.offer(new int[]{nx, ny});
            }
            
        }
    }
}