import UIKit

class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        let str = s.split(separator: " ")
            .filter { $0 != "" }
            .map { $0 }
            .last ?? ""
        
        return str.count
    }
}

let solution = Solution()
solution.lengthOfLastWord("   fly me   to   the moon  ")
