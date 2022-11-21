import UIKit

class Solution {
    func addBinary(_ a: String, _ b: String) -> String {
        let a = String(repeating: "0", count: max(0, b.count - a.count)) + a
        let b = String(repeating: "0", count: max(0, a.count - b.count)) + b
        
        var result = ""
        var carry = 0
        
        for (a, b) in zip(a.reversed(), b.reversed()) {
            let a = Int(String(a)) ?? 0
            let b = Int(String(b)) ?? 0
            let sum = a + b + carry
            result = String(sum % 2) + result
            carry = sum / 2
        }
                          
        if carry == 1 { result = "1" + result }
        
        return result
    }
}

let solution = Solution()
solution.addBinary("11", "1")
