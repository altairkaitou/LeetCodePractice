class Solution {
    public int minGroups(int[][] intervals) {
        int n = intervals.length;

        int[] startAt = new int[n];
        int[] endAt = new int[n];

        for(int i = 0; i < n; i++) {
            startAt[i] = intervals[i][0];
            endAt[i] = intervals[i][1];
        }

        Arrays.sort(startAt);
        Arrays.sort(endAt);

        int end_index = 0;

        int group_count = 0;


        for(int start : startAt) {
            if (start > endAt[end_index]) {
                end_index++;
            } else {
                group_count++;
            }
        }


        return group_count;


        
    }
}