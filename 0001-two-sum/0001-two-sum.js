/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    n = nums.length;
    const map = new Map();
    for (let i = 0; i < n; i++ ) {
        complement = target - nums[i];

        if (map.has(complement)) {
            return [map.get(complement), i]

        }

        map.set(nums[i], i) 
        
    }


    
};