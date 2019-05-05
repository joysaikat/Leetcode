class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        S = S.replace(')(', ')+(')
        #print(S)
        S = S.replace('()', '1')
        #print(S)
        S = S.replace('(', '2*(')
        #print(S)
        return(eval(S))
