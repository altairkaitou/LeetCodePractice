class Solution {
    public int countSeniors(String[] details) {
        int count = 0;
        for (String substr : details) {
            int ages = Integer.parseInt(substr.substring(11, 13));
            if (ages > 60) {
                count++;
            }
        }
        return count;

        
    }
}