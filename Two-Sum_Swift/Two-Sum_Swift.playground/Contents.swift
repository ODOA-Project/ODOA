import UIKit

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dics: [Int:Int] = [:]
        
        for (index, num) in nums.enumerated() {
            let diff = target - num
            if dics.keys.contains(diff) {
                return [dics[diff]!, index]
            }
                   
            dics[num] = index
        }
        
        return []
    }
}

let solution = Solution()
print(solution.twoSum([0, 1, 2, 0], 0))
