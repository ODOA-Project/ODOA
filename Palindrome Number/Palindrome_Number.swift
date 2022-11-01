import UIKit

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x < 0 { return false }
        if x < 10 { return true }
        
        var palindrome = 0
        var copyX = x
        
        while copyX > 0 {
            let quotient = copyX / 10 // 몫
            let remainder = copyX % 10 // 나머지
            let digit = floor(log10(CGFloat(copyX))) // 자릿수
            
            palindrome += remainder * Int(pow(10, digit))
            
            if quotient < 10 {
                palindrome += quotient
                copyX = -1
            } else {
                copyX = quotient
            }
        }
        
        if x == palindrome {
            return true
        } else {
            return false
        }
    }
}


let solutuion = Solution()
print(solutuion.isPalindrome(1))
