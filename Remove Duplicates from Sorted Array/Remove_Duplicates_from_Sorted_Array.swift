import UIKit

class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        nums = Array(Set<Int>(nums)).sorted()
        return nums.count
    }
}

let solution = Solution()
var num = [1, 1, 2]
solution.removeDuplicates(&num)

