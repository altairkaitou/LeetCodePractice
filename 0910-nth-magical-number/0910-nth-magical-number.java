class Solution {
    public int nthMagicalNumber(int n, int a, int b) {
        int MOD = 1000000007;
        long lcm = lcm(a, b);
        long left = 1;
        long right = (long) n * Math.min(a, b);


        while (left < right) {
            long mid = left + (right - left) / 2 ;
            if (calmagical(mid, a, b, lcm) < n) {
                left = mid + 1;
            } else {
                right = mid;
            } 
        }
        return (int) (left % MOD);
    }

        private long lcm(int a, int b) {
            return (long) (a * b) / gcd(a, b);

        }
        private int gcd(int a, int b) {
            if (b == 0) {
                return a;
            }
            return gcd(b, a % b);
        }

        private long calmagical(long x, int a, int b, long lcm) {
            return x/a + x/b - x/lcm ;
        }





        
    
}