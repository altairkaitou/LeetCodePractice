class Solution {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        Integer[] numsarray = Arrays.stream(nums).boxed().toArray(Integer[]::new);

        Arrays.sort(numsarray, new Comparator<Integer>() {
            public int compare(Integer a, Integer b) {
                int mappedA = getMappedvalue(a, mapping);
                int mappedB = getMappedvalue(b, mapping);
                return Integer.compare(mappedA, mappedB);
            }
        });

        return Arrays.stream(numsarray).mapToInt(Integer::intValue).toArray();

        
    }

    private int getMappedvalue(int num, int[] mapping) {
        StringBuilder mappedValue = new StringBuilder();
        String numStr = String.valueOf(num);

        for( char c : numStr.toCharArray()) {
            mappedValue.append(mapping[c - '0']);
        } 

        return Integer.parseInt(mappedValue.toString());
    }
}