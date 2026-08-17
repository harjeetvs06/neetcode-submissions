class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=len(s)
        r=len(t)

        if l!=r:
            return False
        
        return sorted(s)== sorted(t)

        
        


        
        