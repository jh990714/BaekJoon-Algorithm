class Solution {
    public int solution(int[][] sizes) {
        int maxW = 0;
        int maxH = 0;
        
        for (int[] size : sizes) {
            int width = size[0] > size[1] ? size[0] : size[1];
            int height = size[0] > size[1] ? size[1] : size[0];
 
            maxW = width > maxW ? width : maxW;
            maxH = height > maxH ? height : maxH;
        }
        
        return maxW * maxH;
    }
}