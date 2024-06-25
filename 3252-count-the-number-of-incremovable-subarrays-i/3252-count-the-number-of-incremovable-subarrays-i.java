class Solution {
    public int incremovableSubarrayCount(int[] nums) {
        int count = 0;
        int n = nums.length;
        
        for (int left = 0; left < n; left++) {
            for (int right = left; right < n; right++) {

                int[] A = new int[n - (right - left + 1)];
                int idx = 0;
                for (int i = 0; i < left; i++) {
                    A[idx++] = nums[i];
                }
                for (int i = right + 1; i < n; i++) {
                    A[idx++] = nums[i];
                }

    
                boolean valid = true;
                for (int k = 0; k < A.length - 1; k++) {
                    if (A[k] >= A[k + 1]) {
                        valid = false;
                        break;
                    }
                }
                if (valid) {
                    count++;
                }
            }
        }
        
        return count;
        
    }
}