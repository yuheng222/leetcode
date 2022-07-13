class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False
        letters = collections.Counter(magazine)
        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] -= 1
        return True
        