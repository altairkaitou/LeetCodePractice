class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        newstring = sentence.split()
        for i in range(1, len(newstring) + 1):
            if newstring[i - 1].startswith(searchWord):
                return i 
        
        return -1
            
        

        