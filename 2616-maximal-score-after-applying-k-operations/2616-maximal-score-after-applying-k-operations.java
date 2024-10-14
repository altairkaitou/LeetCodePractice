class Solution {
    public long maxKelements(int[] nums, int k) {
        long score = 0;

        PriorityQueue<Long> maxHeap = new PriorityQueue<>((a, b) -> Long.compare(b, a));

        for(int num : nums) {
            maxHeap.add((long) num);
        }

        for(int i = 0; i < k; i++) {
            long maxValue = maxHeap.poll();

            score += maxValue;

            long newValue = (long) Math.ceil(maxValue/ 3.0);
            maxHeap.add(newValue);
        }


        return score;
        
    }
}