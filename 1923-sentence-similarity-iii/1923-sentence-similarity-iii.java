class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] Sen1 = sentence1.split(" ");
        String[] Sen2 = sentence2.split(" ");

        if (Sen1.length > Sen2.length) {
            String[] temp = Sen1;
            Sen1 = Sen2;
            Sen2 = temp;
        }

        int i = 0;
        while(i < Sen1.length && Sen1[i].equals(Sen2[i])) {
            i++;
        }

        int j = 0;
        while(j < Sen1.length && Sen1[Sen1.length - 1 - j].equals(Sen2[Sen2.length - 1 - j])) {
            j++;
        }


        return (i + j) >= Sen1.length;


        
    }
}