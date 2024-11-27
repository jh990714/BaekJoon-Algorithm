import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = new int[]{1,  0, -1, 0};
    static int[] dy = new int[]{0, -1,  0, 1};

    static int n, m;
    static int[][] board;
    static List<Point> cheeses = new ArrayList<>();


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) {
                    cheeses.add(new Point(i, j));
                }
            }
        }

        int time = 0;
        while (!cheeses.isEmpty()) {
            findEdgeAir(new Point(0, 0));
            meltCheese();

            time++;
        }

        System.out.println(time);
    }
    public static void meltCheese() {
        List<Point> meltedCheeses = new ArrayList<>();

        for (Point cheese : cheeses) {
            int x = cheese.getX();
            int y = cheese.getY();

            int airCnt = 0;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

                if (board[nx][ny] == 2) airCnt++;
            }

            if (airCnt >= 2) {
                meltedCheeses.add(cheese);
            }
        }

        for (Point cheese : meltedCheeses) {
            board[cheese.getX()][cheese.getY()] = 0;
        }
        cheeses.removeAll(meltedCheeses);
    }

    public static void printBoard() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void findEdgeAir(Point start) {
        Queue<Point> que = new LinkedList<>();
        que.add(start);

        boolean[][] visited = new boolean[n][m];
        visited[start.getX()][start.getY()] = true;
        
        board[start.getX()][start.getY()] = 2;

        while (!que.isEmpty()) {
            Point curP = que.poll();
            int x = curP.getX();
            int y = curP.getY();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
                if (visited[nx][ny] == true) continue;
                if (board[nx][ny] == 1) continue;

                board[nx][ny] = 2;
                visited[nx][ny] = true;
                que.add(new Point(nx, ny));
            }
        }
    }


    static class Point {
        private int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() { return this.x; }
        public int getY() { return this.y; }
    }

}
