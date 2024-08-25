import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int[] map = new int[y+1];
        Arrays.fill(map, -1);
        
        map[x] = 0;
        for (int i = x; i <= y; i++) {
            if (map[i] == -1) {
                continue;
            }
            
            if ((i + n) <= y) {
                map[i+n] = map[i+n] == -1 ? map[i] + 1 : Math.min(map[i+n], map[i] + 1);
            }
            
            if ((i * 2) <= y) {
                map[i*2] = map[i*2] == -1 ? map[i] + 1 : Math.min(map[i*2], map[i] + 1);
            }
            
            if ((i * 3) <= y) {
                map[i*3] = map[i*3] == -1 ? map[i] + 1 : Math.min(map[i*3], map[i] + 1);
            }
        }
        
        return map[y];
    }
}