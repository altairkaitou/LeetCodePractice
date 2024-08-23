class Solution {
    private static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a%b);
    }

    private static int[] addFraction(int num1, int denom1, int num2, int denom2) {
        int num = num1 * denom2 + num2 * denom1;
        int denom = denom1 * denom2;
        int g = gcd(Math.abs(num), denom);
        return new int[]{num/g, denom / g};
    }

    public String fractionAddition(String expression) {


        List<String> tokens = new ArrayList<>();
        int i = 0;
        int n = expression.length();
        while(i < n) {
            int start = i;
            if (expression.charAt(i) == '-' || expression.charAt(i) == '+') {
                i++;
            }
            while(i < n && expression.charAt(i) != '+' && expression.charAt(i) != '-') {
                i++;
            }

            tokens.add(expression.substring(start, i));

        }

        int numo = 0;
        int demo = 1;

        for(String token : tokens) {
            String[] parts = token.split("/");
            int num = Integer.parseInt(parts[0]);
            int dem = Integer.parseInt(parts[1]);

            int[] result = addFraction(numo, demo, num, dem);
            numo = result[0];
            demo = result[1];
        }

        if (demo == 1) {
            return numo + "/1";
        } else {
            return numo + "/" + demo;
        }
    }
}