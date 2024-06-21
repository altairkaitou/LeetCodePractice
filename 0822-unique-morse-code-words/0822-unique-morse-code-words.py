class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        res = []

        for word in words:
            morse = ""
            for c in word:
                morse += morse_code[ord(c) - 97]
            if morse not in res:
                res.append(morse)
        return len(res)
        