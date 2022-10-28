import UIKit

class Solution {
    func romanToInt(_ s: String) -> Int {
        let romanToIntDics: [Character:Int] = ["I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000]
        var changeS = s.replacingOccurrences(of: "IV", with: "IIII")
            .replacingOccurrences(of: "IX", with: "VIIII")
            .replacingOccurrences(of: "XL", with: "XXXX")
            .replacingOccurrences(of: "XC", with: "LXXXX")
            .replacingOccurrences(of: "CD", with: "CCCC")
            .replacingOccurrences(of: "CM", with: "DCCCC")
        var sum = 0
        
        var sum = changeS.map({ (ch: Character) -> Int in return romanToIntDics[ch]! }).reduce(0, +)
            sum += romanToIntDics[ch]!
        }

        return sum
    }
}

let solution = Solution()
print(solution.romanToInt("MCMXCIV"))
