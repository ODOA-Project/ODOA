import UIKit

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        
        var result: [Int] = []
        
        for (index, num) in nums.enumerated() {
            if (nums.count == index) {
                return []
            }
            
            let nextNum = nums[index + 1]
            let sum = num + nextNum
            
            if sum == target {
                result.append(num)
                result.append(nextNum)
                break
            }
        }
        
        return result
    }
}

let solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 26))

