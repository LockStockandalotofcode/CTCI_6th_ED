class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dic = {2: 'abc', 3: 'def', 4:'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        res = []
        if not digits:
            return res

        def dfs(index: int, curr_path: str, res: list[str]) -> None:
            # base condition or termination condition
            if index == len(digits):
                res.append(curr_path)
                return
            mapping_to_curr_digit = dic[int(digits[index])]
            for char in mapping_to_curr_digit:
                dfs(index + 1, curr_path + char, res)

        dfs(0, '', res)
        return res