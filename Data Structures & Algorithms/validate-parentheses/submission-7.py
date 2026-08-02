class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        open_str = ["[" , "{" , "("]
        close_str =  ["]", "}" , ")"]
        pairs = {"{":"}","[":"]","(":")"}
        result = []
        for ch in s:            
            if ch in open_str:
                result.append(ch)
            elif ch in close_str:
                if result == []:
                    return False
                if pairs[result[-1]] != ch :
                    return False
                else:
                    result.pop()
        return result == []