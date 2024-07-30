class Solution {
    public int minimumDeletions(String s) {
        
        int count_b = 0;
        int min_deletions = 0;
        for (char c : s.toCharArray()) {
            if (c == 'b') {
                count_b++;
            } else if (c == 'a'){
                if (count_b > 0) {
                    min_deletions++;
                    count_b--;
        
                }
            }
        }
        return min_deletions;


        
    }
}