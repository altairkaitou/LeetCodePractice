class Solution {
    public int minExtraChar(String s, String[] dictionary) {
        int n = s.length();
        Set<String> wordSet = new HashSet<>(Arrays.asList(dictionary));

        int[] dp = new int[n + 1];
        Arrays.fill(dp, n + 1);

        dp[0] = 0;

        for(int i = 1; i <= n; i++) {
            for(int j = 0; j < i;j++) {
                String subs = s.substring(j,i);
                if (wordSet.contains(subs)) {
                    dp[i] = Math.min(dp[i], dp[j]);
                } else {
                    dp[i] = Math.min(dp[i], dp[j] + (i - j));
                }
            }
        }

        return dp[n];
        
    }
}