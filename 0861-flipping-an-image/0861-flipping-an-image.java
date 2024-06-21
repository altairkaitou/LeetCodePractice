class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for(int[] row : image) {
            flipping(row);
            inverted(row);

        }
        return image;
    }
    private void flipping(int[] row) {
        int left = 0;
        int right = row.length - 1;
        while (left < right) {
            int temp = row[left];
            row[left] = row[right];
            row[right] = temp;
            left++;
            right--;
        }
    }

    private void inverted(int[] row)  {
        for(int i = 0; i < row.length; i ++) {
            row[i] = 1 - row[i];

        }
    }
}