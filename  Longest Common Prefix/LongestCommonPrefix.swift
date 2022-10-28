import UIKit
import Foundation

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        if strs == [] { return "" }
        
        var prefixStr: String = strs.min(by: { $0.count < $1.count })!
        var temp: String = ""
        
        for str in strs {
            for (index, ch) in prefixStr.enumerated() {
                let ch = String(ch)
                
                if index == 0 && !str.starts(with: ch) { return "" }
               
                let checker = temp + ch
                if !str.starts(with: checker) { break }
                
                temp = checker
            }
            
            prefixStr = temp
            temp = ""
        }
        
        return prefixStr
    }
}

let solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
