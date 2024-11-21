import java.util.*;

class Solution {
    int[][] dp;

    public int solution(int[][] triangle) {
        int n = triangle.length;
        dp = new int[n + 1][n + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < triangle[i].length; j++) {
                dp[i+1][j+1] = Math.max(dp[i][j], dp[i][j+1]) + triangle[i][j];
            }
        }

        int max = 0;
        for (int i = 0; i < dp[n].length; i++) {
            max = Math.max(max, dp[n][i]);
        }

        return max;
    }
}
