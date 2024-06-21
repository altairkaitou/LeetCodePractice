class Solution {
    public int[] shortestToChar(String s, char c) {
        List<Integer> cPosition = new ArrayList<>();
        int[] result = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == c) {
                cPosition.add(i);
            }
        }

        int currPos = 0; 

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                result[i] = 0;
                currPos++;
            }
            else if (i < cPosition.get(0)) {
                result[i] = cPosition.get(0) - i;

            } else if (i > cPosition.get(cPosition.size() - 1)) {
                result[i] = i - cPosition.get(cPosition.size() - 1);
            }
            else {
                result[i] = Math.min((cPosition.get(currPos) - i), (i - cPosition.get(currPos - 1)));

            }
        }
        return result;
        
    }
}