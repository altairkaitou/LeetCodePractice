class Solution {
    public int minLength(String s) {
        Stack<Character> Charstack = new Stack<>();

        for(int i = 0 ; i < s.length(); i++) {
            char curr_char = s.charAt(i);
            if (Charstack.isEmpty()) {
                Charstack.push(curr_char);
                continue;
            }

            if (curr_char == 'B' && Charstack.peek() == 'A') {
                Charstack.pop();
            } else if (curr_char == 'D' && Charstack.peek() == 'C') {
                Charstack.pop();
            } else {
                Charstack.push(curr_char);
            }
        }


        return Charstack.size();


        

        
        
    }
}