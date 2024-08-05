class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> hash_appear = new HashMap<>();

        for (String v : arr) {
            hash_appear.put(v, hash_appear.getOrDefault(v, 0) + 1);
        }

        for (String v : arr) {
            if (hash_appear.get(v) == 1) {
                k--;

                if (k == 0) {
                    return v;
                }
            }
        }

        return ""; 


        
    }
}