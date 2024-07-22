class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        Arrays.sort(nums);

        //function to reversed the array
        reverseArr(nums);

        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int subSum = 0;
        List<Integer> subsequence = new ArrayList<>();

        for (int num : nums) {
            subSum += num;
            subsequence.add(num);

            if (subSum > totalSum - subSum) {
                break;
            }
        }

        return subsequence;
    }

    public static void reverseArr(int[] arrays){
        int left = 0;
        int right = arrays.length - 1;
        while (left < right) {
            int temp = arrays[left];
            arrays[left] = arrays[right];
            arrays[right] = temp;
            left++;
            right--;
        }
    }
}