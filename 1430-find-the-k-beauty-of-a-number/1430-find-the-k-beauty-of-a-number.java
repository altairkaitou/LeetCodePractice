class Solution {
    public int divisorSubstrings(int num, int k) {
        StringBuilder s= new StringBuilder("");
        int result = 0;
        s.append(num);
        for (int i = 0; i < s.length() - k + 1; i++ ) {
            String t = s.substring(i, i + k);
            int x = Integer.parseInt(t);
            if (x != 0 && num% x == 0) {
                result++;
            }
        }
        return result;

        
    }
}