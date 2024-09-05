class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int required_sum = mean * (rolls.length + n);
        int current_sum = 0;

        for (int i = 0; i < rolls.length; i++) {
            current_sum += rolls[i];
        }

        int missing_sum = required_sum - current_sum;

        if (missing_sum < n*1 || missing_sum > n*6) {
            return new int[0];
        }

        int[] result = new int[n];

        int remaining_sum = missing_sum - n;

        for(int i = 0;i < n;i++) {
            int add = Math.min(remaining_sum, 5);
            result[i] = 1 + add;
            remaining_sum -= add;
        }


        return result;


        
    }
}