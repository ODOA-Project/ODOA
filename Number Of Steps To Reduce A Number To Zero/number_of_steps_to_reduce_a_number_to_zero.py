class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        입력 받은 숫자가 0이 될 때까지의 step을 계산한다.
        """
        step: int = 0
        while num != 0:
            step += 1
            if num % 2 == 1:
                num = num - 1
            else:
                num = num / 2
        return step
        