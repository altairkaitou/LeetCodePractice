class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        List<Integer> result = new ArrayList<>();
        
        for (int i = 0; i < arr2.length; i++) {
            for (int j = 0; j < arr1.length; j++) {
                if (arr2[i] == arr1[j]) {
                    result.add(arr1[j]);
                    arr1[j] = -1;
                }
            }
        }


        List<Integer> remain = new ArrayList<>();

        for(int i = 0; i < arr1.length; i++) {
            if (arr1[i] > -1) {
                remain.add(arr1[i]);
            }
        }

        Collections.sort(remain);
        result.addAll(remain);

        int[] finalresult = new int[result.size()];

        for (int i = 0; i < result.size(); i++) {
            finalresult[i] = result.get(i);
        }

        return finalresult;

    }
}