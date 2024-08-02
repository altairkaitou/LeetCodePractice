class Solution {
    public int maxDistToClosest(int[] seats) {
        int n = seats.length;
        int last_person = -1;
        int max_dist = 0;

        for (int i = 0; i < n; i++) {
            if (seats[i] == 1) {
                if (last_person == -1) {
                    max_dist = i;
                } else {
                    max_dist = Math.max(max_dist, (i - last_person) / 2);

                }
                last_person = i;
            }
        }


        if (seats[n - 1] == 0) {
            max_dist = Math.max(max_dist, n - 1 - last_person);
        }

        return max_dist;
        
    }
}