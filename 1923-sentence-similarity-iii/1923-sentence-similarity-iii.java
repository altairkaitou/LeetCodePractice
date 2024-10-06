class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] word1 = sentence1.split(" ");
        String[] word2 = sentence2.split(" ");

        if (word1.length > word2.length) {
            String[] temp = word1;
            word1 = word2;
            word2 = temp;
        }


        int i = 0;
        while(i < word1.length && word1[i].equals(word2[i])) {
            i++;
        }

        int j = 0;
        while(j < word1.length && word1[word1.length - 1- j].equals(word2[word2.length - 1- j])) {
            j++;
        }

        return (i + j) >= word1.length;
        
    }
}