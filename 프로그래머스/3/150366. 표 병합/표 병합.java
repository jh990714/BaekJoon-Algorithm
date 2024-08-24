import java.util.*;

class Solution {
    public String[] map = new String[2500];
    public int[] parentMap = new int[2500];
    
    public Solution() {
        for (int i = 0; i < parentMap.length; i++) {
            parentMap[i] = i;
        }
    }
    
    public String[] solution(String[] commands) {
        List<String> result = new ArrayList<>();
        
        for (String command : commands) {
            String[] splitCommand = command.split(" ");
            
            String order = splitCommand[0];
            
            switch (order) {
                case "UPDATE":
                    if (splitCommand.length == 4) {
                        int row = Integer.parseInt(splitCommand[1]) - 1;
                        int col = Integer.parseInt(splitCommand[2]) - 1;
                        String value = splitCommand[3];
                        
                        update(row, col, value);
                    } else {
                        String value1 = splitCommand[1];
                        String value2 = splitCommand[2];
                        
                        update(value1, value2);
                    }
                    break;
                case "MERGE":
                    int row1 = Integer.parseInt(splitCommand[1]) - 1;
                    int col1 = Integer.parseInt(splitCommand[2]) - 1;
                    int row2 = Integer.parseInt(splitCommand[3]) - 1;
                    int col2 = Integer.parseInt(splitCommand[4]) - 1;
                    
                    merge(row1, col1, row2, col2);
                    break;
                case "UNMERGE":
                    int uRow = Integer.parseInt(splitCommand[1]) - 1;
                    int uCol = Integer.parseInt(splitCommand[2]) - 1;
                    
                    unmerge(uRow, uCol);
                    break;
                case "PRINT":
                    int pRow = Integer.parseInt(splitCommand[1]) - 1;
                    int pCol = Integer.parseInt(splitCommand[2]) - 1;
                    
                    result.add(print(pRow, pCol));
                    break;
            }
        }
        
        return result.toArray(new String[0]);
    }
    
    public void update(int row, int column, String value) {
        int root = findRoot(getIndex(row, column));
        map[root] = value;
    }
    
    public void update(String value1, String value2) {
        for (int i = 0; i < map.length; i++) {
            if (map[i] != null && map[i].equals(value1)) {
                map[i] = value2;
            }
        }
    }
    
    public void merge(int row1, int column1, int row2, int column2) {
        int root1 = findRoot(getIndex(row1, column1));
        int root2 = findRoot(getIndex(row2, column2));
        
        if (root1 == root2) return;
        
        String value1 = map[root1];
        String value2 = map[root2];
        String mergeValue = value1 != null ? value1 : value2;
        
        map[root1] = mergeValue;
        map[root2] = null;
        
        updateParent(root2, root1);
    }
    
    public void updateParent(int oldRoot, int newRoot) {
        for (int i = 0; i < parentMap.length; i++) {
            if (findRoot(i) == oldRoot) {
                parentMap[i] = newRoot;
            }
        }
    }
    
    public void unmerge(int row, int column) {
        int root = findRoot(getIndex(row, column));
        String value = map[root];
        
        for (int i = 0; i < parentMap.length; i++) {
            if (findRoot(i) == root) {
                parentMap[i] = i;
                map[i] = null;
            }
        }
        
        map[getIndex(row, column)] = value;
    }
    
    public String print(int row, int column) {
        int root = findRoot(getIndex(row, column));
        return map[root] != null ? map[root] : "EMPTY";
    }
    
    public int findRoot(int n) {
        if (parentMap[n] != n) {
            parentMap[n] = findRoot(parentMap[n]);
        }
        return parentMap[n];
    }
    
    public int getIndex(int row, int column) {
        return row * 50 + column; // Adjust based on 50x50 grid
    }
}
