import java.util.*;

class Solution {
    Queue<Point> que;
    boolean[][] visited;
    
    int[] dx = new int[]{1,  0, -1, 0};
    int[] dy = new int[]{0, -1,  0, 1};
    
    public int solution(int[][] game_board, int[][] table) {
        List<Puzzle> emptySpaces = findPieces(game_board, 0);
        List<Puzzle> tablePieces = findPieces(table, 1);
        
        int totalFilled = 0;
        for (Puzzle space : emptySpaces) {
            for (Puzzle piece : tablePieces) {
                if (space.matches(piece)) {
                    totalFilled += piece.size();
                    tablePieces.remove(piece);
                    
                    break;
                }
            }
        }
        
        return totalFilled;
    }
    
    private List<Puzzle> findPieces(int[][] board, int target) {
        List<Puzzle> pieces = new ArrayList<>();
        visited = new boolean[board.length][board[0].length];
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == target && visited[i][j] == false) {
                    Puzzle puzzle = bfs(board, new Point(i, j), target);
                    pieces.add(puzzle);
                }
            }
        }
        
        return pieces;
    }
    
    private Puzzle bfs(int[][] board, Point start, int target) {
        que = new LinkedList<>();
        que.offer(start);
        
        visited[start.getX()][start.getY()] = true;
        
        Puzzle puzzle = new Puzzle();
        while (!que.isEmpty()) {
            Point point = que.poll();
            
            int x = point.getX();
            int y = point.getY();
            
            puzzle.add(point);
            
            for (int i = 0; i < dx.length; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || ny < 0 || nx >= board.length || ny >= board[0].length) continue;
                if (visited[nx][ny] || board[nx][ny] != target) continue;
                
                visited[nx][ny] = true;
                que.offer(new Point(nx, ny));

            }
            
        }
        puzzle.normalize();
        return puzzle;

    }
    
    class Puzzle {
        List<Point> points;
        
        public Puzzle() {
            points = new ArrayList<>();
        }
        
        public List<Point> getPoints() { return this.points; }
        
        public void add(Point point) {
            points.add(point);
        }
        
        int size() {
            return points.size();
        }

        void normalize() {
            int minX = points.stream().mapToInt(p -> p.x).min().orElse(0);
            int minY = points.stream().mapToInt(p -> p.y).min().orElse(0);
            for (Point p : points) {
                p.x -= minX;
                p.y -= minY;
            }
            points.sort((a, b) -> a.getX() == b.getX() ? a.getY() - b.getY() : a.getX() - b.getX());
        }

        boolean matches(Puzzle other) {
            for (int i = 0; i < 4; i++) {
                if (this.points.equals(other.getPoints()))
                    return true;
                other.rotate();
            }
            return false;
        }
        
        void rotate() {
            for (Point p : points) {
                int temp = p.x;
                p.x = p.y;
                p.y = -temp;
            }
            normalize();
        }
        
        @Override
        public String toString() {
            return "Puzzle{" +
                   "points=" + points +
                   '}';
        }
        
    }
    
    class Point {
        int x;
        int y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        public int getX() { return this.x; }
        public int getY() { return this.y; }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
        
        @Override
        public String toString() {
            return "(" + x + ", " + y + ")";
        }
        
    }
}