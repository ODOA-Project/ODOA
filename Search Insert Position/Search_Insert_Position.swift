import UIKit

class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var arr = nums
        arr.append(target)
        arr = Array(Set<Int>(arr)).sorted()
        
        var position = arr.count < 2 ? 0 : arr.count / 2
    
        while position >= 0 && position < arr.count {
            if arr[position] == target {
                return position
            } else if arr[position] > target {
                position -= 1
            } else {
                position += 1
            }
        }
    
        return position
    }
}

let solution = Solution()
solution.searchInsert([1, 3], 1)



