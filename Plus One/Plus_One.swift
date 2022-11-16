import UIKit

class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var addValue = 1
        
        var reverseDigit = digits.reversed().map { digit -> Int in
            let sum = digit + addValue
            addValue = sum / 10
            
            return sum % 10
        }
        
        if addValue != 0 {
            reverseDigit.append(1)
        }
        
        return reverseDigit.reversed()
    }
}

let solution = Solution()
solution.plusOne([7,2,8,5,0,9,1,2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7,4,0,0,6])
