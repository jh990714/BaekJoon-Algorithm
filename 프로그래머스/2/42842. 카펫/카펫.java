class Solution {
    public int[] solution(int brown, int yellow) {
        int carpetSize = brown + yellow;
        int[] answer = new int[2];
        
        for (int i = 3; i <= carpetSize; i++) {
            if (carpetSize % i != 0) continue;
            
            int carpetW = carpetSize / i;
            int carpetH = i;

            int yellowW = carpetW - 2;
            int yellowH = carpetH - 2;

            if (yellowW * yellowH == yellow) {
                answer[0] = carpetW;
                answer[1] = carpetH;
                
                break;
            }
        
        }
        
        return answer;
    }

}