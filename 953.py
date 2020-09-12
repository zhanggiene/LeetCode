class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict={}
        for i in range(len(order)):
            orderDict[order[i]]=i
        #print(orderDict)
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>len(words[i+1])-1:
                    return False
                elif orderDict[words[i][j]]>orderDict[words[i+1][j]]:
                    return False
                elif orderDict[words[i][j]]<orderDict[words[i+1][j]]:
                    break
                elif orderDict[words[i][j]]==orderDict[words[i+1][j]]:
                    continue
                
            
        return True