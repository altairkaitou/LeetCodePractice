class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        Map<Integer, Integer> weightMap = new HashMap<>();

        for(int[] item : items1) {
            int value = item[0];
            int weight = item[1];
            weightMap.put(value, weightMap.getOrDefault(value, 0) + weight);
        }

        for(int[] item: items2) {
            int value = item[0];
            int weight = item[1];
            weightMap.put(value, weightMap.getOrDefault(value, 0) + weight);
        }

        List<int[]> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry: weightMap.entrySet()) {
            result.add(new int[]{entry.getKey(), entry.getValue()});
        }

        result.sort((a, b) -> Integer.compare(a[0], b[0]));


        List<List<Integer>> finalresult = new ArrayList<>();
        for (int[] item : result) {
            List<Integer> templist = new ArrayList<>();
            templist.add(item[0]);
            templist.add(item[1]);
            finalresult.add(templist);

        }
        return finalresult;
        
    }
}