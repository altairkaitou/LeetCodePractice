class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int[] cloneArr = arr.clone();
        Arrays.sort(cloneArr);

        Map<Integer, Integer> rankMap = new HashMap<>();
        int rank = 1;

        for(int i = 0 ; i < arr.length; i++) {
            if(!rankMap.containsKey(cloneArr[i])) {
                rankMap.put(cloneArr[i], rank++);
            }
        }

        int[] result = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            result[i] = rankMap.get(arr[i]);
        }


        return result;
        
        
    }
}