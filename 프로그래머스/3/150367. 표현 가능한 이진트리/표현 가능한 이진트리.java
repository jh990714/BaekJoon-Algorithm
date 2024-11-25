import java.util.*;

class Solution {
    public int[] solution(long[] numbers) {
        List<Integer> answer = new ArrayList<>();
        
        for (long number : numbers) {
            String binary = Long.toBinaryString(number);
            
            String fullBinaryNum = fullBinary(binary, getTreeNode(binary));
            
            if (isBinaryTree(fullBinaryNum)) {
                answer.add(1);
            } else {
                answer.add(0);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    public int getTreeNode(String binary) {
        int length = binary.length();
        int nodeCount = 1;
        int level = 1;
        
        while (length > nodeCount) {
            level *= 2;
            nodeCount += level;
        }
        
        return nodeCount;
    }
    
    public String fullBinary(String binary, int nodeCount) {
        int length = binary.length();
        int offSet = nodeCount - length;
        
        return "0".repeat(offSet) + binary;
    }
    
    public boolean isBinaryTree(String binary) {
        int length  = binary.length();
        if (length == 0) return true;
        
        int root = length / 2;
        String leftBinary = binary.substring(0, root);
        String rightBianry = binary.substring(root+1);
        
        if (binary.charAt(root) == '0') {
            if (leftBinary.contains("1")) {
                return false;
            }
            if (rightBianry.contains("1")) {
                return false;
            }
        }
        
        return isBinaryTree(leftBinary) && isBinaryTree(rightBianry);
    }
    
}