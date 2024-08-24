class Solution {
    public int solution(int storey) {
        // 0, 1, 2, 3, 4 -> +
        // 6, 7, 8, 9 -> -, 다음 숫자 +1
        // 5일때 그 다음 숫자 검사 -> 5이상 +1
        int result = 0;
        while (storey > 0) {
            int digit = storey % 10;
            storey = storey / 10;
            
            if (digit == 5) {
                if (storey % 10 >= 5) {
                    result += (10 - digit);
                    storey ++;
                } else {
                    result += (10 - digit);
                }
            } else if (digit > 5) {
                result += (10 - digit);
                storey ++;
            } else {
                result += digit;
            }
        }
        return result;
    }
}