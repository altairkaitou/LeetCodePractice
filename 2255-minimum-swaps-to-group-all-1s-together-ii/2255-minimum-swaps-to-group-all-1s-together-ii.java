class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int count_one = 0;
        int[] extended_nums = new int[2 * n];
        System.arraycopy(nums, 0, extended_nums, 0, n);
        System.arraycopy(nums, 0, extended_nums, n, n);

        for (int num : nums) {
            count_one += num;
        }

        if (count_one == 0 || count_one == n) {
            return 0;
        }

        int currentOneWin = 0;
        int maxOneWin = 0;

        for (int i = 0; i < count_one; i++) {
            currentOneWin += extended_nums[i];
        }

        maxOneWin = currentOneWin;
        for (int i = count_one; i < 2 * n; i++) {
            currentOneWin += extended_nums[i] - extended_nums[i - count_one];
            maxOneWin = Math.max(maxOneWin, currentOneWin);

        }

        return count_one - maxOneWin;


    
    }
}