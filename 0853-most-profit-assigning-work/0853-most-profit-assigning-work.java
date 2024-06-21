class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int j = 0;
        int best = 0;
        int result = 0;

        List<int[]> temp = new ArrayList<>();

        for (int i = 0; i < difficulty.length; i++ ) {
            temp.add(new int[] {difficulty[i], profit[i]});
        }

        Collections.sort(temp, (a,b) -> a[0] - b[0]);
        Arrays.sort(worker);

        for(int work : worker) {
            while (j < temp.size() && work >= temp.get(j)[0]){
                best = Math.max(best, temp.get(j)[1]);
                j++;
            }
            result += best;
        }
        return result;
        
    }
}