class Solution {
    public boolean lemonadeChange(int[] bills) {
        int five_dollars = 0;
        int ten_dollars = 0;
        
        for (int cus: bills) {
            if (cus == 5) {
                five_dollars++;
            } else if (cus == 10) {
                if (five_dollars > 0) {
                    ten_dollars++;
                    five_dollars--;
                } else {
                    return false;
                }
            } else {
                if (five_dollars > 0 && ten_dollars > 0) {
                    five_dollars--;
                    ten_dollars--;
                } else if (five_dollars >= 3) {
                    five_dollars -= 3;
                } else {
                    return false;
                }
            }
        }
        return true;
    }
}