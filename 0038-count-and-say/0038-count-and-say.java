class Solution {
    public String countAndSay(int n) {
        String out = "1";

        for(int i = 0; i < n - 1; i++) {
            char prevChar = out.charAt(0);
            int count = 1;
            StringBuilder temp = new StringBuilder();

            for (int j = 1; j < out.length(); j++) {
                if (prevChar == out.charAt(j)) {
                    count++;
                } else {
                    temp.append(Integer.toString(count)).append(prevChar);
                    prevChar = out.charAt(j);
                    count = 1;
                }
            }

            temp.append(Integer.toString(count)).append(prevChar);
            out = temp.toString();

            
        }
        return out;




        
    }
}