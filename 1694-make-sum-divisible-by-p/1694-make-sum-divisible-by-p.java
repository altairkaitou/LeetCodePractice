class Solution {
    public int minSubarray(int[] nums, int p) {
        long total_sum = 0;

        for(int i = 0; i < nums.length; i++) {
            total_sum += nums[i];
        }

        int Reminder = (int)(total_sum %p);

        if (Reminder == 0) {
            return 0;
        }

        HashMap<Integer, Integer> prefixMap = new HashMap<>();
        prefixMap.put(0, -1);
        long prefixSum = 0 ;


        int minLength = nums.length;

        for (int i = 0 ; i < nums.length; i++) {
            prefixSum += nums[i];
            int currentMod = (int)(prefixSum % p);
            int targetMod = (currentMod - Reminder + p) % p;

            if (prefixMap.containsKey(targetMod)) {
                minLength = Math.min(minLength, i - prefixMap.get(targetMod));
            }

            prefixMap.put(currentMod, i);
        }

        return minLength == nums.length ? -1 : minLength;


        
    }
}