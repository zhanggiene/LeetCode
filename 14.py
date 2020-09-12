class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=[]
        if len(strs)==0 or len(strs[0])==0:
            return ""
        for i in range(len(strs[0])):
            letter=strs[0][i]
            print(common)
            for j in range(len(strs)):
                if i>=len(strs[j]) or letter!=strs[j][i]:
                    return "".join(common)
            common.append(letter)
        return "".join(common)
        