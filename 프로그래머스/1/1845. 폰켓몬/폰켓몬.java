import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        int numsSize = nums.length / 2;

        HashSet<Integer> poketNum = new HashSet<>();

        for (int num : nums) {
            poketNum.add(num);
        }

        if (numsSize > poketNum.size()) {
            return poketNum.size();
        } else {
            return numsSize;
        }
    }
}