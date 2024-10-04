class Solution {
    public long dividePlayers(int[] skill) {
        int n = skill.length;
        int totalSum = 0;
        int[] frequency = new int[1001];

        if (n == 2) {
            return skill[0] * skill[1];
        }

        for (int num : skill) {
            totalSum += num;
        }

        if (totalSum % (n/2) != 0) {
            return -1;
        }
        int perTeamSkill = totalSum/(n/2);

        for(int num : skill) {
            frequency[num]++;
        }

        long chemistry = 0 ;

        for(int s : skill) {
            int partnerSkill = perTeamSkill - s;
            if (frequency[partnerSkill] > 0) {
                chemistry += (long)s * (long)partnerSkill;
                frequency[partnerSkill]--;
            } else return -1;
        }


        return chemistry/2;






        
    }
}