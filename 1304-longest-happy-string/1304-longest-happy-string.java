class Solution {
    public String longestDiverseString(int a, int b, int c) {

        PriorityQueue<int[]> preQueue = new PriorityQueue<>((x,y ) -> y[0] - x[0]);

        if (a > 0) preQueue.offer(new int[] {a, 'a'});
        if (b > 0) preQueue.offer(new int[] {b, 'b'});
        if (c > 0) preQueue.offer(new int[] {c, 'c'});

        StringBuilder result = new StringBuilder();

        while ( !preQueue.isEmpty()) {
            int[] first = preQueue.poll();

            if (result.length() >= 2 && result.charAt(result.length() - 1) == first[1] &&
                result.charAt(result.length() - 2) == first[1]) {
                    if (preQueue.isEmpty()) {
                        break;
                    }

                    int[] second = preQueue.poll();
                    result.append((char) second[1]);
                    second[0]--;

                    if (second[0] > 0) {
                        preQueue.offer(second);
                    }

                    preQueue.offer(first);

                } else {
                    result.append((char) first[1]);
                    first[0]--;

                    if (first[0] > 0) {
                        preQueue.offer(first);
                    }
                }
        }


        return result.toString();
        
    }
}