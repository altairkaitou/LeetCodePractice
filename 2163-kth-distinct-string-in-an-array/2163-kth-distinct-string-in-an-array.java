class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> hash_arr = new HashMap<>();

        for(String v : arr) {
            hash_arr.put(v, hash_arr.getOrDefault(v, 0) + 1);
        }

        for(String v : arr) {
            if (hash_arr.get(v) == 1) {
                k--;
                if (k == 0) {
                    return v;
                }
            }
        }
        return "";
    }
}