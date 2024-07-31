class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int n = books.length;
        int[] dp = new int[n + 1];
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }

        for (int i = 1; i <= n; i++) {
            int totalThickness = 0;
            int maxHeight = 0;
            for(int j = i - 1; j >= 0; j--) {
                totalThickness += books[j][0];
                if (totalThickness > shelfWidth) {
                    break;
                }

                maxHeight = Math.max(maxHeight, books[j][1]);
                dp[i] = Math.min(dp[i], dp[j] + maxHeight);
            }

        }

        return dp[n];



        
    }
}