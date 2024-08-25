import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int[] myScore = scores[0];
        int myTotal = myScore[0] + myScore[1];
        int maxTeamScore = 0;
        int rank = 1;
        
        Arrays.sort(scores, (a, b) ->  a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]);
        
        for (int[] score : scores) {
            int teamScore = score[1];
            
            if (maxTeamScore <= teamScore) {
                maxTeamScore = teamScore;
                
                if (myTotal < score[0] + score[1]) rank++; 
            } else {
                if (score.equals(myScore)) return -1;
            }
        }
        
        return rank;
    }
}

/* 
3 2
3 2
2 1
2 2 
1 4 
*/