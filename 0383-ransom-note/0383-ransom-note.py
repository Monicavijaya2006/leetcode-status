class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        x = True
        for i in ransomNote:
            if ransomNote.count(i)>magazine.count(i):
                x = False
        return x