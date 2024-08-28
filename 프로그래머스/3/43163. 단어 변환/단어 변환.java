import java.util.*;

public class Solution {
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }

        return bfs(begin, target, words);
    }
    
    private int bfs(String begin, String target, String[] words) {
        Queue<Word> queue = new LinkedList<>();
        queue.offer(new Word(begin, 0));

        boolean[] visited = new boolean[words.length];

        while (!queue.isEmpty()) {
            Word current = queue.poll();
            
            String currentWord = current.word;
            int currentStep = current.step;

            if (currentWord.equals(target)) {
                return currentStep;
            }

            for (int i = 0; i < words.length; i++) {
                if (!visited[i] && canTransform(currentWord, words[i])) {
                    visited[i] = true;
                    queue.offer(new Word(words[i], currentStep + 1));
                }
            }
        }

        return 0;
    }
    
    private boolean canTransform(String word1, String word2) {
        int count = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                count++;
            }
        }
        return count == 1;
    }

    class Word {
        String word;
        int step;

        Word(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }

}
