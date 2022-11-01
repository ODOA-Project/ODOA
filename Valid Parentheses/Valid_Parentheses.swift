import UIKit

class Solution {
    func isValid(_ s: String) -> Bool {
        let parentheses = [")":"(", "}":"{", "]":"["]
        
        var arr : [String] = []
        
        for char in s {
            let str = String(char)
            
            if let parenth = parentheses[str] {
                let arrStr = arr.popLast()
                if  arrStr != parenth { return false }
            } else {
                arr.append(str)
            }
        }
        
        if arr == [] {
            return true
        } else {
            return false
        }
    }
}

let solution = Solution()
print(solution.isValid("{[]}"))
