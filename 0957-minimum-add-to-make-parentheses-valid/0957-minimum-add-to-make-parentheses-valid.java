class Solution {
    public int minAddToMakeValid(String s) {
         Stack<Character> stack = new Stack<>();
         int count = 0;
         for(char c : s.toCharArray()) {
            if ( c == '(') {
                stack.push(c);
            } else if (c == ')') {
                if(!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    count++;
                }
            }
           
         }

         count += stack.size();
         return count;
        
    }
}