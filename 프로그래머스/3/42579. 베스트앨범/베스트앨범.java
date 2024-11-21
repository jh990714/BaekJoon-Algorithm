import java.util.*;
import java.util.stream.Collectors;

class Solution {

    public int[] solution(String[] genres, int[] plays) {
        Song[] songs = new Song[genres.length];
        for (int i = 0; i < genres.length; i++) {
            Song song = new Song(i, plays[i], genres[i]);
            songs[i] = song;
        }
        
        Map<String, Integer> genre_plays = new HashMap<>();
        for (Song song : songs) {
            String genre = song.getGenre();
            int play = song.getPlay();
            
            genre_plays.put(genre, genre_plays.getOrDefault(genre, 0) + play);
        }
        
        List<String> sorted_genre = genre_plays.entrySet().stream()
                                .sorted((e1, e2) -> e2.getValue() - e1.getValue())
                                .map(Map.Entry::getKey)
                                .collect(Collectors.toList());
        
        List<Integer> answers = new ArrayList<>();
        for (String genre : sorted_genre) {
            List<Song> genreSongs = Arrays.stream(songs)
                    .filter(song -> song.getGenre().equals(genre))
                    .sorted((s1, s2) -> s2.getPlay() - s1.getPlay())
                    .collect(Collectors.toList());
            
            genreSongs.stream()
                  .limit(2)
                  .map(Song::getId)
                  .forEach(answers::add);
        }
        
        return answers.stream().mapToInt(Integer::intValue).toArray();
    }
}

class Song {
    int id;
    int play;
    String genre;
    
    Song(int id, int play, String genre) {
        this.id = id;
        this.play = play;
        this.genre = genre;
    }
    
    public int getId() { return this.id; }
    public int getPlay() { return this.play; }
    public String getGenre() { return this.genre; }
}