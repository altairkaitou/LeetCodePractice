class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:

        #a,c,e,g case:
        if coordinates[0] == 'a' or coordinates[0] == 'c' or coordinates[0] == 'e' or coordinates[0] =='g':
            if int(coordinates[1]) % 2 == 0:
                return True
            elif int(coordinates[1]) % 2 != 0:
                return False
        
        else:
            if (int(coordinates[1])) % 2 == 0:
                return False 
            elif int(coordinates[1]) % 2 != 0:
                return True 

        