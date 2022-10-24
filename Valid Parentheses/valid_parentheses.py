class Solution:
    def isValid(self, parentheses_list: str) -> bool:
        str_stack = []
        parentheses_dict = {"}": "{", "]": "[", ")": "("}
        for parentheses in parentheses_list:
            if parentheses in "{[(":
                str_stack.append(parentheses)
            elif (
                len(str_stack) == 0
                or parentheses_dict.get(parentheses) != str_stack.pop()
            ):
                return False

        return len(str_stack) == 0


if __name__ == "__main__":
    Solution().isValid("]]")
