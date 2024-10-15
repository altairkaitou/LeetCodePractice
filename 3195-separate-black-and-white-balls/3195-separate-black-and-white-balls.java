class Solution {
    public long minimumSteps(String s) {
        int white = 0;
        long result =0 ;
      

        for( int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                result += (long) white;
            } else if( s.charAt(i) == '1') {
                white++;
            }
        }


        return result;

        
    }
}