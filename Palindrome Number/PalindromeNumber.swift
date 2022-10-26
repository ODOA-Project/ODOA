import UIKit

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 { return false }
        if x < 10 { return true }
        
        var palindrome: [Int] = []
        var copyX = x
        var flag = true
        
        while flag {
            let quotient = copyX / 10 // 몫
            let remainder = copyX % 10 // 나머지
            
            palindrome.append(remainder)
            
            if quotient < 10 {
                palindrome.append(quotient)
                flag = false
            } else {
                copyX = quotient
            }
        }
        
        if palindrome == palindrome.reversed() {
            return true
        } else {
            return false
        }
    }
}


let solutuion = Solution()
print(solutuion.isPalindrome(1))
