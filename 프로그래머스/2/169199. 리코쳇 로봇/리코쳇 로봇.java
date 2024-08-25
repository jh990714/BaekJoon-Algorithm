import java.util.*;

class Point {
    private int x, y, move;
    
    public Point(int x, int y, int move) {
        this.x = x;
        this.y = y;
        this.move = move;
    }
    
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    public int getMove() {
        return move;
    }
}

class Solution {
    // 상 하 좌 우
    int[][] direction = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    int N, M;
    
    public int solution(String[] board) {
        // bfs 탐색으로 최단거리
        N = board.length;
        M = board[0].length();
        
        Point start = null;
        Point end = null;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i].charAt(j) == 'R') {
                    start = new Point(i, j, 0);
                } else if (board[i].charAt(j) == 'G') {
                    end = new Point(i, j, 0);
                }
            }
        }
        
        return bfs(board, start, end);
    }
    
    public int bfs(String[] board, Point start, Point end) {
        Queue<Point> q = new LinkedList<>();
        q.add(start);
        
        boolean[][] visited = new boolean[N][M];
        visited[start.getX()][start.getY()] = true;
        
        while (!q.isEmpty()) {
            Point curPoint = q.poll();
            
            if (curPoint.getX() == end.getX() && curPoint.getY() == end.getY()) {
                return curPoint.getMove();
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = curPoint.getX();
                int ny = curPoint.getY();
                
                // 해당 방향으로 쭉 이동
                while (true) {
                    int tempX = nx + direction[i][0];
                    int tempY = ny + direction[i][1];
                    
                    if (tempX < 0 || tempX >= N || tempY < 0 || tempY >= M || board[tempX].charAt(tempY) == 'D') {
                        break;
                    }
                    
                    nx = tempX;
                    ny = tempY;
                }
                
                if (visited[nx][ny]) continue;
                
                q.add(new Point(nx, ny, curPoint.getMove() + 1));
                visited[nx][ny] = true;
            }
        }
        
        return -1;
    }
}
